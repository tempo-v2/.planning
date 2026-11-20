"""Create one new prototype directory using the selected Tempo binary and compiled UI."""
import argparse
import json
from pathlib import Path
import shlex
import subprocess
import tempfile
from urllib.request import Request, urlopen


def post(origin, path, **data):
    request = Request(f"{origin}/api/{path}", data=json.dumps(data).encode(),
                      headers={"Content-Type": "application/json"})
    with urlopen(request, timeout=20) as response:
        reply = json.load(response)
    if reply.get("errors") or reply.get("status") == "error":
        raise ValueError(reply)
    return reply


def seed(origin):
    dataset = post(origin, "repertoires", command="list")["dataset_id"]

    def add_book(name, color, lines):
        pgn = "\n\n".join(f'[Event "{label}"]\n[Result "*"]\n\n{moves} *' for label, moves in lines)
        book = dict(dataset_id=dataset, name=name, learner_color=color, pgn=pgn)
        preview = post(origin, "repertoires", command="preview", **book)
        saved = post(origin, "repertoires", command="save", token=preview["token"], **book)
        assert any(row["name"] == name for row in saved["repertoires"])

    add_book("Italian repertoire", "white", [
        ("Two Knights", "1. e4 e5 2. Nf3 Nc6 3. Bc4 Nf6 4. d3 Bc5 5. O-O d6 6. c3 O-O 7. Re1"),
        ("Giuoco Piano", "1. e4 e5 2. Nf3 Nc6 3. Bc4 Bc5 4. c3 Nf6 5. d3 d6 6. O-O"),
        ("Hungarian", "1. e4 e5 2. Nf3 Nc6 3. Bc4 Be7 4. d4 d6 5. Nc3"),
    ])
    first = post(origin, "study", command="next")
    taught = post(origin, "study", command="acknowledge", dataset_id=dataset,
                  attempt_id=first["attempt_id"], expected_revision=first["revision"],
                  submission_id="lab-lesson", answer={"uci": first["lesson"]["move_uci"]})
    assert taught["status"] == "complete"
    add_book("Caro-Kann repertoire", "black", [
        ("Advance", "1. e4 c6 2. d4 d5 3. e5 Bf5 4. Nf3 e6"),
        ("Exchange", "1. e4 c6 2. d4 d5 3. exd5 cxd5 4. Bd3 Nc6"),
    ])
    for index, (opponent, moves, result) in enumerate([
        ("Avery", "1. e4 e5 2. Nf3 Nc6 3. Bb5 a6 4. Ba4 Nf6 5. O-O Be7 6. Re1 b5 7. Bb3 d6", "0-1"),
        ("Robin", "1. e4 e5 2. Nf3 Nf6 3. Bc4 Nc6 4. d3 Bc5 5. O-O d6 6. c3 O-O 7. Re1 a6 8. Bb3", "1/2-1/2"),
        ("Morgan", "1. e4 e5 2. Nf3 Nc6 3. Bc4 Be7 4. d4 d6 5. Nc3 Nf6 6. O-O O-O 7. Re1", "1-0"),
    ]):
        pgn = (f'[Event "Evening rapid"]\n[Site "Club"]\n[Date "2026.11.{16 + index}"]\n'
               f'[Round "{1 + index}"]\n[White "Andy"]\n[Black "{opponent}"]\n'
               f'[Result "{result}"]\n\n{moves} {result}')
        imported = post(origin, "games/import", dataset_id=dataset, command_id=f"club-game-{index}",
                        learner="Andy", pgn=pgn)
        assert imported["new_games"] == 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("tempo", type=Path)
    parser.add_argument("ui_dist", type=Path)
    parser.add_argument("new_directory", type=Path)
    parser.add_argument("--empty", action="store_true")
    args = parser.parse_args()
    binary, ui, folder = (path.resolve() for path in (args.tempo, args.ui_dist, args.new_directory))
    if not binary.is_file() or not (ui / "index.html").is_file():
        parser.error("Supply the built Tempo executable and UI directory.")
    folder.mkdir(mode=0o700, parents=True, exist_ok=False)
    database = folder / "study.sqlite"
    subprocess.run([binary, "init", database], cwd=folder, check=True)
    command = [str(binary), "serve", str(database), str(ui), "0"]
    if not args.empty:
        with tempfile.TemporaryFile(mode="w+") as log:
            server = subprocess.Popen(command, cwd=folder, stdout=subprocess.PIPE, stderr=log, text=True)
            try:
                origin = server.stdout.readline().strip().removeprefix("Tempo study at ")
                if not origin.startswith("http://127.0.0.1:"):
                    log.seek(0)
                    raise RuntimeError(f"Disposable server did not start. {log.read()}")
                seed(origin)
            finally:
                server.terminate()
                server.wait(timeout=10)
    print(f"Start from {folder} with a free local port. For an automatically assigned port run\n{shlex.join(command)}")


if __name__ == "__main__":
    main()
