import os
from warnings import filterwarnings
from Yone import OWNER_ID, dispatcher
from Yone.Plugins.disable import DisableAbleCommandHandler
from telegram import Update, ParseMode
from telegram.ext import CallbackContext,Filters, run_async
from matplotlib import pyplot as plt
import Yone.Database.users_sql as usersql
from Yone.Database import cust_filters_sql as filtersql
from Yone.Database import warns_sql as warnsql
from Yone.Database import blacklist_sql as blacklistsql


def pstate(update: Update, context: CallbackContext):
    bot = context.bot
    message = update.effective_message
    labels = ["Users", "Filters", "Warnings", "Blacklists"]

    data = [usersql.num_users(), filtersql.num_filters(), warnsql.num_warns(), blacklistsql.num_blacklist_filters() ]

    acrossData = [usersql.num_chats(), filtersql.num_chats(),warnsql.num_warn_chats(), blacklistsql.num_blacklist_filter_chats() ]
    fig, ax = plt.subplots()

    # Creating plot
    ax.bar(labels, data, color="red")
    for x, y, p in zip(labels, data, acrossData):
            plt.text(x, y, p)

    fname = "chart.jpg"
    ofile = open(fname, "rb")
    # show plot
    fig.savefig(fname)
    message.reply_photo(ofile,
                     caption="Made By @Yone_Robot",
                     parse_mode=ParseMode.HTML,)
    plt.close(fig)




STATES_HANDLER = DisableAbleCommandHandler("stat", pstate, run_async=True)
dispatcher.add_handler(STATES_HANDLER)
 
 
