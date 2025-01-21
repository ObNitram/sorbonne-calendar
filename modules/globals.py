from modules.algav import get_algav_calendars
from modules.archi import get_archi_calendars
from modules.ares import get_ares_calendars
from modules.dlp import get_dlp_calendars
from modules.noyau import get_noyau_calendars
from modules.pscr import get_pscr_calendars
from modules.sc import get_sc_calendars
from modules.vlsi import get_vlsi_calendars
from modules.mlbda import get_mlbda_calendars
from modules.pnl import get_pnl_calendars
from modules.ar import get_ar_calendars
from modules.srcs import get_srcs_calendars
from modules.sftr import get_sftr_calendars
from modules.sas import get_sas_calendars
from modules.anglais_sar import get_anglais_sar_calendars

MODULE_FUNCTIONS = {
    "RES.ARES": get_ares_calendars,
    "SAR.NOYAU": get_noyau_calendars,
    "SAR.PSCR": get_pscr_calendars,
    "SAR.PNL": get_pnl_calendars,
    "SAR.AR": get_ar_calendars,
    "SAR.SRCS": get_srcs_calendars,
    "SAR.SFTR": get_sftr_calendars,
    "SAR.SAS": get_sas_calendars,
    "SAR.ANGLAIS": get_anglais_sar_calendars,
    "SESI.ARCHI": get_archi_calendars,
    "SESI.VLSI": get_vlsi_calendars,
    "SFPN.SC": get_sc_calendars,
    "STL.ALGAV": get_algav_calendars,
    "STL.DLP": get_dlp_calendars,
    "DAC.MLBDA": get_mlbda_calendars,
    "SESI.MULTI": get_multi_calendars,
    "SESI.IOC": get_ioc_calendars
}
