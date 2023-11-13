import numpy as np
from scipy.spatial import KDTree
import matplotlib.pyplot as plt

basePath_tng100="/home/cossim/IllustrisTNG/TNG100-1/"   # on ssh
particle_dm_mass=0.00050557*10**10   #M_sun/h
boxlen_100=75000    #ckpc/h

#对于一个group获得其subhalo的ID，包含它自己
def get_subhaloID(GroupID, GroupFirstSub):
    if GroupFirstSub[GroupID]==-1:
        return 0
    return np.arange(GroupFirstSub[GroupID],GroupFirstSub[GroupID+1])

#在考虑循环边界条件的情况下计算粒子间的距离
def get_pos_diff(pos_a,pos_b,boxlen):
    diff1=pos_b-pos_a
    diff2=pos_b-pos_a
    diff2[np.where(np.abs(diff1)>boxlen/2)]=diff1[np.where(np.abs(diff1)>boxlen/2)]-np.sign(diff1[np.where(np.abs(diff1)>boxlen/2)])*boxlen
    return diff2

#通过 offset 文件：第group_id中的subgroup_id 对应的粒子坐标
#先读 group 包含的所有粒子 再分配到 subhalo
def get_pid_group_subhalo(subgroup_id, group_id,pid_subhalo,parttype_id, parttype="dm"):
    return [pid_subhalo[subgroup_id,parttype_id[parttype]]-pid_group[group_id,parttype_id[parttype]],
            pid_subhalo[subgroup_id+1,parttype_id[parttype]]-pid_group[group_id,parttype_id[parttype]]]





#画图
def plot_histogram(ax, x, y, bins, c="k", label="", alpha=1):
    mean,edge=np.histogram(x,bins=bins,weights=y)
    N,edge=np.histogram(x,bins=bins)
    ax.plot((edge[1:]+edge[:-1])/2,mean/N,c, label=label, alpha=alpha)
    ax.plot((edge[1:]+edge[:-1])/2,-mean/N,c+":", alpha=alpha)

def plot_hist_a_N(ax, a, bins=100, c="k", xlabel=""):
    ax.hist(a,bins=bins,c=c)
    ax.set_xlabel(xlabel)
    
