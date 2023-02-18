

from MonarchMusic import monarchdb


async def put(
    chat_id,
    title,
    duration,
    videoid,
    file_path,
    ruser,
    user_id,
):
    put_f = {
        "title": title,
        "duration": duration,
        "file_path": file_path,
        "videoid": videoid,
        "req": ruser,
        "user_id": user_id,
    }
    get = monarchdb.get(chat_id)
    if get:
        monarchdb[chat_id].append(put_f)
    else:
        monarchdb[chat_id] = []
        monarchdb[chat_id].append(put_f)
