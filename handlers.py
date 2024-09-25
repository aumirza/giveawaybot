from hydrogram.types import Message
from db import add_coupon, fetch_latest_coupon,update_coupon,fetch_coupon_count ,clear_all_redeemed_coupons, clear_all_unredeemed_coupons,clear_all_coupons


async def admin_start_handler(client, message:Message):
    text = 'Hi! Admin  \n\n \
Total redeemed coupons: {coupons_count["redeemed"]}  \n \
Total unredeemed coupons:  {coupons_count["unredeemed"]} \n\n \
All available commands    \n \
    /clear_redeemed - Clear redeemed coupons \n \
    /clear_unredeemed - Clear unredeemed coupons \n  \
    /clear_all - Clear all coupons \n \ '
    # /display_all - Display all coupons \n'
    await message.reply(text=text)
    
async def clear_redeemed_handler(client, message:Message):
    await clear_all_redeemed_coupons()
    await message.reply(text="All redeemed coupons cleared!")
    

async def clear_unredeemed_handler (client, message:Message):
    await clear_all_unredeemed_coupons()
    await message.reply(text="All unredeemed coupons cleared!")

async def clear_all_handler (client, message:Message):
    await clear_all_coupons()
    await message.reply(text="All coupons cleared!")

# async def display_all_handler (client, message:Message):
#     coupons_count = await fetch_coupon_count()
#     text = f'Welcome to the giveaway bot! '
#     await message.reply(text=text)

async def listen_handler(client, message:Message):
    # save coupons to database
    coupon = {"coupon":message.text , "redeemed":False}
    return await add_coupon(coupon)

async def giveaway_handler(client,message:Message):
    # fetch the latest coupon from db
    unredeemed_coupon = await fetch_latest_coupon()
    if not unredeemed_coupon: return await message.reply(text="All coupons already redeemed!")
    await update_coupon(unredeemed_coupon,True)
    return await message.reply(text=unredeemed_coupon.get("coupon"))
    