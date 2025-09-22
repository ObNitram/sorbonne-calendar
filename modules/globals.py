
# Master 1
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
from modules.multi import get_multi_calendars
from modules.ioc import get_ioc_calendars
from modules.anglais_sar import get_anglais_sar_calendars

# Master 2
from modules.secres import get_secres_calendars
from modules.ara import get_ara_calendars
from modules.datacloud import get_datacloud_calendars
from modules.nvm import get_nvm_calendars
from modules.astre import get_astre_calendars
from modules.pacc import get_pacc_calendars
from modules.smc import get_smc_calendars

MODULE_FUNCTIONS = {
    # Master 1
    "M1-RES.ARES": get_ares_calendars,
    "M1-SAR.NOYAU": get_noyau_calendars,
    "M1-SAR.PSCR": get_pscr_calendars,
    "M1-SAR.PNL": get_pnl_calendars,
    "M1-SAR.AR": get_ar_calendars,
    "M1-SAR.SRCS": get_srcs_calendars,
    "M1-SAR.SFTR": get_sftr_calendars,
    "M1-SAR.SAS": get_sas_calendars,
    "M1-SAR.ANGLAIS": get_anglais_sar_calendars,
    "M1-SESI.ARCHI": get_archi_calendars,
    "M1-SESI.VLSI": get_vlsi_calendars,
    "M1-SFPN.SC": get_sc_calendars,
    "M1-STL.ALGAV": get_algav_calendars,
    "M1-STL.DLP": get_dlp_calendars,
    "M1-DAC.MLBDA": get_mlbda_calendars,
    "M1-SESI.MULTI": get_multi_calendars,
    "M1-SESI.IOC": get_ioc_calendars,
    
    # Master 2
    "M2-RES.SECRES": get_secres_calendars,
    "M2-SAR.ARA": get_ara_calendars,
    "M2-SAR.DATACLOUD": get_datacloud_calendars,
    "M2-SAR.NVM": get_nvm_calendars,
    "M2-SAR.ASTRE": get_astre_calendars,
    "M2-SESI.PACC": get_pacc_calendars,
    "M2-SESI.SMC": get_smc_calendars,
}
