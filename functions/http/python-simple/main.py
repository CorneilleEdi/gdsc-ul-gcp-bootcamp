import functions_framework


@functions_framework.http
def handler(request):
    word: string | None = request.args.get("word")
    if not word:
        return "No word provided", 400
    return {"word": word[::-1]}
