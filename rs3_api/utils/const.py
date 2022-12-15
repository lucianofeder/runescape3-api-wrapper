from enum import Enum, unique

BASE_URL = "https://secure.runescape.com"


@unique
class Skills(str, Enum):
    OVERALL = "overall",
    ATTACK = "attack",
    DEFENCE = "defence",
    STRENGTH = "strength",
    CONSTITUTION = "constitution",
    RANGED = "ranged",
    PRAYER = "prayer",
    MAGIC = "magic",
    COOKING = "cooking",
    WOODCUTTING = "woodcutting",
    FLETCHING = "fletching",
    FISHING = "fishing",
    FIREMAKING = "firemaking",
    CRAFTING = "crafting",
    SMITHING = "smithing",
    MINING = "mining",
    HERBLORE = "herblore",
    AGILITY = "agility",
    THIEVING = "thieving",
    SLAYER = "slayer",
    FARMING = "farming",
    RUNECRAFTING = "runecrafting",
    HUNTER = "hunter",
    CONSTRUCTION = "construction",
    SUMMONING = "summoning",
    DUNGEONEERING = "dungeoneering",
    DIVINATION = "divination",
    INVENTION = "invention",
    ARCHEOLOGY = "archeology"


@unique
class Minigames(str, Enum):
    BOUNTY_HUNTER = "Bounty Hunter",
    BH_ROGUES = "B.H. Rogues",
    DOMINNION_TOWER = "Dominion Tower",
    THE_CRUCIBLE = "The Crucible",
    CASTLE_WARS = "Castle Wars games",
    BA_ATTACKERS = "B.A. Attackers",
    BA_DEFENDERS = "B.A. Defenders",
    BA_COLLECTORS = "B.A. Collectors",
    BA_HEALERS = "B.A. Healers",
    DUEL_TOURNAMENT = "Duel Tournament",
    MOBILISING_ARMIES = "Mobilising Armies",
    CONQUEST = "Conquest",
    FIST_OF_GUTHIX = "Fist of Guthix",
    GG_ATHLETICS = "GG: Athletics",
    GG_RESOURCE_RACE = "GG: Resource Race",
    WE2_ARMADYL_LIFETIME = "WE2: Armadyl Lifetime Contribution",
    WE2_BANDOS_LIFETIME = "WE2: Bandos Lifetime Contribution",
    WE2_ARMADYL_PVP_KILLS = "WE2: Armadyl PvP kills",
    WE2_BANDOS_PVP_KILLS = "WE2: Bandos PvP kills",
    HEIST_GUARD_LEVEL = "Heist Guard Level",
    HEIST_ROBBER_LEVEL = "Heist Robber Level",
    CFP_5_GAME_AVG = "CFP: 5 game average",
    AF15_COW_TIPPING = "AF15: Cow Tipping",
    AF15_RATS_KILLED_AFTER_QUEST = "AF15: Rats killed after the miniquest",
    RUNESCORE = "RuneScore",
    CLUE_EASY = "Clue Scrolls Easy",
    CLUE_MEDIUM = "Clue Scrolls Medium",
    CLUE_HARD = "Clue Scrolls Hard",
    CLUE_ELITE = "Clue Scrolls Elite",
    CLUE_MASTER = "Clue Scrolls Master"


@unique
class AccountTypes(str, Enum):
    NORMAL = 'normal'
    IRONMAN = 'ironman'
    HARDCORE = 'hardcore_ironman'
