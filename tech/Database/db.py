from motor.motor_asyncio import AsyncIOMotorClient as MongoClient

MONGO_DB_URI = "mongodb+srv://khansagunawan157:UDg0BmbVKhHlOpGv@cluster0.zyfsas1.mongodb.net/?retryWrites=true&w=majority"
MONGODB_CLI = MongoClient(MONGO_DB_URI)
db = MONGODB_CLI.zentech

async def is_served_user(user_id: int) -> bool:
    user = await userdb.find_one({"user_id": user_id})
    if not user:
        return False
    return True
  
async def add_member_zentech(user_id: int, nomor_telfon: int, string_session: str, nama_pengguna: str):
    is_served = await is_served_user(user_id)
    if is_served:
        return
    return await userdb.insert_one({"user_id": user_id, "nomor_telfon": nomor_telfon, "string_session": string_session,  "nama_pengguna": nama_pengguna})
