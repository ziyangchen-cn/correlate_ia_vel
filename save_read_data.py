import sys
import os
import time
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from tqdm import tqdm
import camb
from camb import model, initialpower
import h5py
from scipy.spatial import KDTree

sys.path.append("/home/chenzy/code/")
import illustris_python as il

from basical_para import *    #basePath_tng100, particle_dm_mass, boxlen_100(kpc/h)



def save_group(snapNum):
    #Halos in TNG100-1
    #Group中第一个subhalo对应的坐标
    GroupFirstSub=il.groupcat.loadHalos(basePath=basePath_tng100, snapNum=snapNum, fields="GroupFirstSub")
    #Group的坐标 ckpc/h
    GroupPos=il.groupcat.loadHalos(basePath=basePath_tng100, snapNum=snapNum, fields="GroupPos")
    #Group的速度 km/s/a
    GroupVel=il.groupcat.loadHalos(basePath=basePath_tng100, snapNum=snapNum, fields="GroupVel")
    #mass 200   10^10 M_sun/h
    Group_M_Mean200=il.groupcat.loadHalos(basePath=basePath_tng100, snapNum=snapNum, fields="Group_M_Mean200")
    # R mean 200 ckpc/h
    Group_R_Mean200=il.groupcat.loadHalos(basePath=basePath_tng100, snapNum=snapNum, fields="Group_R_Mean200")

    save_name = "TNG100-1_Group_"+str(snapNum).zfill(3)+".npz"
    np.savez(save_name, GroupFirstSub=GroupFirstSub, GroupPos=GroupPos, GroupVel=GroupVel, Group_M_Mean200=Group_M_Mean200, Group_R_Mean200=Group_R_Mean200)

def read_group(snapNum):
    #Halos in TNG100-1
    read_name = "TNG100-1_Group_"+str(snapNum).zfill(3)+".npz"
    d = np.load(read_name)
    GroupFirstSub = d["GroupFirstSub"]
    GroupPos = d["GroupPos"]
    GroupVel = d["GroupVel"]
    Group_M_Mean200 = d["Group_M_Mean200"]
    Group_R_Mean200 = d["Group_R_Mean200"]

    return GroupFirstSub, GroupPos, GroupVel, Group_M_Mean200, Group_R_Mean200
    

def save_subgroup(snapNum):
    #subhalo in TNG100-1
    #subhalo的坐标 ckpc/h
    SubhaloPos=il.groupcat.loadSubhalos(basePath=basePath_tng100, snapNum=99, fields="SubhaloPos")
    #subhalo是否可靠
    SubhaloFlag=il.groupcat.loadSubhalos(basePath=basePath_tng100, snapNum=99, fields="SubhaloFlag")
    #subhalo 的速度 km/s
    SubhaloVel=il.groupcat.loadSubhalos(basePath=basePath_tng100, snapNum=99, fields="SubhaloVel")
    # all mass
    SubhaloMass=il.groupcat.loadSubhalos(basePath=basePath_tng100, snapNum=99, fields="SubhaloMass")
    # mass type
    SubhaloMassType=il.groupcat.loadSubhalos(basePath=basePath_tng100, snapNum=99, fields="SubhaloMassType")
    SubhaloMass_Star=SubhaloMassType[:,4]

    save_name = "TNG100-1_SubGroup_"+str(snapNum).zfill(3)+".npz"
    np.savez(save_name, SubhaloPos=SubhaloPos, SubhaloFlag=SubhaloFlag, SubhaloVel=SubhaloVel, SubhaloMass=SubhaloMass, SubhaloMassType=SubhaloMassType)


def read_subgroup(snapNum):
    #Halos in TNG100-1
    read_name = "TNG100-1_SubGroup_"+str(snapNum).zfill(3)+".npz"
    d = np.load(read_name)
    SubhaloPos = d["SubhaloPos"]
    SubhaloFlag = d["SubhaloFlag"]
    SubhaloVel = d["SubhaloVel"]
    SubhaloMass = d["SubhaloMass"]
    SubhaloMassType = d["SubhaloMassType"]
    SubhaloMass_Star=SubhaloMassType[:,4]

    return SubhaloPos, SubhaloFlag, SubhaloVel, SubhaloMass, SubhaloMass_Star

def save_offset(snapNum):
    #offset file
    f = h5py.File("/home/cossim/IllustrisTNG/TNG100-1/postprocessing/offsets/offsets_"+str(snapNum).zfill(3)+".hdf5", "r")
    pid_group=f["Group/SnapByType"][:]
    pid_subhalo=f["Subhalo/SnapByType"][:]
    save_name = "TNG100-1_offset_"+str(snapNum).zfill(3)+".npz"
    np.savez(save_name, pid_group=pid_group, pid_subhalo=pid_subhalo)

def read_offest(snapNum):
    read_name = "TNG100-1_offset_"+str(snapNum).zfill(3)+".npz"
    d = np.load(read_name)
    pid_group= d["pid_group"]
    pid_subhalo = d["pid_subhalo"]
    parttype_id={"gas":0,"dm":1,"star":4}
    return pid_group, pid_subhalo, parttype_id


if __name__ == "__main__":
    snapNum = 99
    save_subgroup(snapNum)
    save_group(snapNum)
    save_offset(snapNum)




