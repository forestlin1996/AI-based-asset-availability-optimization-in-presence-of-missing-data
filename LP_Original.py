# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 22:19:00 2020

@author: LIN CHUAN
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import gurobipy
from gurobipy import GRB

# Creat the Model
MODEL = gurobipy.Model()

# Create Variables
x11 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 1(A319) to Edinburgh') 
x12 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 1(A319) to Glasgow')
x13 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 1(A319) to Aberdeen')
x14 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 1(A319) to Belfast')
x15 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 1(A319) to Manchester')
x21 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 2(A319) to Edinburgh')
x22 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 2(A319) to Glasgow')
x23 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 2(A319) to Aberdeen')
x24 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 2(A319) to Belfast')
x25 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 2(A319) to Manchester')
x31 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 3(A319) to Edinburgh')
x32 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 3(A319) to Glasgow')
x33 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 3(A319) to Aberdeen')
x34 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 3(A319) to Belfast')
x35 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 3(A319) to Manchester')
x41 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 4(A319) to Edinburgh')
x42 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 4(A319) to Glasgow')
x43 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 4(A319) to Aberdeen')
x44 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 4(A319) to Belfast')
x45 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 4(A319) to Manchester')
x51 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 5(A319) to Edinburgh')
x52 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 5(A319) to Glasgow')
x53 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 5(A319) to Aberdeen')
x54 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 5(A319) to Belfast')
x55 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 5(A319) to Manchester')
x61 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 6(A320) to Edinburgh')
x62 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 6(A320) to Glasgow')
x63 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 6(A320) to Aberdeen')
x64 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 6(A320) to Belfast')
x65 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 6(A320) to Manchester')
x71 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 7(A320) to Edinburgh')
x72 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 7(A320) to Glasgow')
x73 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 7(A320) to Aberdeen')
x74 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 7(A320) to Belfast')
x75 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 7(A320) to Manchester')
x81 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 8(A320) to Edinburgh')
x82 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 8(A320) to Glasgow')
x83 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 8(A320) to Aberdeen')
x84 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 8(A320) to Belfast')
x85 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 8(A320) to Manchester')
x91 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 9(A320) to Edinburgh')
x92 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 9(A320) to Glasgow')
x93 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 9(A320) to Aberdeen')
x94 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 9(A320) to Belfast')
x95 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 9(A320) to Manchester')
x101 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 10(A320) to Edinburgh')
x102 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 10(A320) to Glasgow')
x103 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 10(A320) to Aberdeen')
x104 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 10(A320) to Belfast')
x105 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 10(A320) to Manchester')
x111 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 11(A320) to Edinburgh')
x112 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 11(A320) to Glasgow')
x113 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 11(A320) to Aberdeen')
x114 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 11(A320) to Belfast')
x115 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 11(A320) to Manchester')
x121 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 12(A320) to Edinburgh')
x122 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 12(A320) to Glasgow')
x123 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 12(A320) to Aberdeen')
x124 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 12(A320) to Belfast')
x125 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 12(A320) to Manchester')
x131 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 13(A320) to Edinburgh')
x132 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 13(A320) to Glasgow')
x133 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 13(A320) to Aberdeen')
x134 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 13(A320) to Belfast')
x135 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 13(A320) to Manchester')
x141 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 14(A320) to Edinburgh')
x142 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 14(A320) to Glasgow')
x143 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 14(A320) to Aberdeen')
x144 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 14(A320) to Belfast')
x145 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 14(A320) to Manchester')
x151 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 15(A321) to Edinburgh')
x152 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 15(A321) to Glasgow')
x153 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 15(A321) to Aberdeen')
x154 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 15(A321) to Belfast')
x155 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 15(A321) to Manchester')
x161 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 16(A321) to Edinburgh')
x162 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 16(A321) to Glasgow')
x163 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 16(A321) to Aberdeen')
x164 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 16(A321) to Belfast')
x165 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 17(A321) to Manchester')
x171 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 17(A321) to Edinburgh')
x172 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 17(A321) to Glasgow')
x173 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 17(A321) to Aberdeen')
x174 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 17(A321) to Belfast')
x175 = MODEL.addVar(lb=0, ub=gurobipy.GRB.INFINITY, vtype=gurobipy.GRB.CONTINUOUS, name='Aircraft 17(A321) to Manchester')

# Identify Variable Index
A319_Cost_Per_Hour = 3590.444444
A320_Cost_Per_Hour = 3682.055556
A321_Cost_Per_Hour = 3929.846167
A319_PartCosts_Percentage = 0.0820
A320_PartCosts_Percentage = 0.1
A321_PartCosts_Percentage = 0.1145

# Identify Fixed Index
Edinburgh_Hours_Normalization = 1.417
Glasgow_Hours_Normalization = 1.5
Aberdeen_Hours_Normalization = 1.583
Belfast_Hours_Normalization =  1.333
Manchester_Hours_Normalization = 1

# Update all Elements
MODEL.update()

# Create Objective Function
MODEL.setObjective(A319_Cost_Per_Hour * (Edinburgh_Hours_Normalization * (x11+x21+x31+x41+x51) + Glasgow_Hours_Normalization * (x12+x22+x32+x42+x52) + Aberdeen_Hours_Normalization * (x13+x23+x33+x43+x53) + Belfast_Hours_Normalization * (x14+x24+x34+x44+x54) + Manchester_Hours_Normalization * (x15+x25+x35+x45+x55)) + A320_Cost_Per_Hour * (Edinburgh_Hours_Normalization * (x61+x71+x81+x91+x101+x111+x121+x131+x141) + Glasgow_Hours_Normalization * (x62+x72+x82+x92+x102+x112+x122+x132+x142) + Aberdeen_Hours_Normalization * (x63+x73+x83+x93+x103+x113+x123+x133+x143) + Belfast_Hours_Normalization * (x64+x74+x84+x94+x104+x114+x124+x134+x144) + Manchester_Hours_Normalization * (x65+x75+x85+x95+x105+x115+x125+x135+x145)) + A321_Cost_Per_Hour * (Edinburgh_Hours_Normalization * (x151+x161+x171) + Glasgow_Hours_Normalization * (x152+x162+x172) + Aberdeen_Hours_Normalization * (x153+x163+x173) + Belfast_Hours_Normalization * (x154+x164+x174) + Manchester_Hours_Normalization * (x155+x165+x175)),GRB.MINIMIZE)

# Create Constraint Functions
MODEL.addConstr(144 * (x11 + x21 + x31 + x41 + x51) + 180 * (x61 + x71 + x81 + x91 + x101 + x111 + x121 + x131 + x141) + 220 * (x151 + x161 + x171) >= 11969210, name='Edinburgh Customer Demand Yearly')
MODEL.addConstr(144 * (x12 + x22 + x32 + x42 + x52) + 180 * (x62 + x72 + x82 + x92 + x102 + x112 + x122 + x132 + x142) + 220 * (x152 + x162 + x172) >= 8650080, name='Glasgow Customer Demand Yearly')
MODEL.addConstr(144 * (x13 + x23 + x33 + x43 + x53) + 180 * (x63 + x73 + x83 + x93 + x103 + x113 + x123 + x133 + x143) + 220 * (x153 + x163 + x173) >= 6922890, name='Aberdeen Customer Demand Yearly')
MODEL.addConstr(144 * (x14 + x24 + x34 + x44 + x54) + 180 * (x64 + x74 + x84 + x94 + x104 + x114 + x124 + x133 + x144) + 220 * (x154 + x164 + x174) >= 6685750, name='Belfast Customer Demand Yearly')
MODEL.addConstr(144 * (x15 + x25 + x35 + x45 + x55) + 180 * (x65 + x75 + x85 + x95 + x105 + x115 + x125 + x134 + x145) + 220 * (x155 + x165 + x175) >= 5542010, name='Manchester Customer Demand Yearly')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x11 + Glasgow_Hours_Normalization * x12 + Aberdeen_Hours_Normalization * x13 + Belfast_Hours_Normalization * x14 + Manchester_Hours_Normalization * x15) <= (39240 - 4033), name ='Aircraft1 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x21 + Glasgow_Hours_Normalization * x22 + Aberdeen_Hours_Normalization * x23 + Belfast_Hours_Normalization * x24 + Manchester_Hours_Normalization * x25) <= (39240 - 4033), name ='Aircraft2 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x31 + Glasgow_Hours_Normalization * x32 + Aberdeen_Hours_Normalization * x33 + Belfast_Hours_Normalization * x34 + Manchester_Hours_Normalization * x35) <= (39240 - 4033), name ='Aircraft3 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x41 + Glasgow_Hours_Normalization * x42 + Aberdeen_Hours_Normalization * x43 + Belfast_Hours_Normalization * x44 + Manchester_Hours_Normalization * x45) <= (39240 - 4033), name ='Aircraft4 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x51 + Glasgow_Hours_Normalization * x52 + Aberdeen_Hours_Normalization * x53 + Belfast_Hours_Normalization * x54 + Manchester_Hours_Normalization * x55) <= (39240 - 4033), name ='Aircraft5 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x61 + Glasgow_Hours_Normalization * x62 + Aberdeen_Hours_Normalization * x63 + Belfast_Hours_Normalization * x64 + Manchester_Hours_Normalization * x65) <= (39240 - 4033), name ='Aircraft6 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x71 + Glasgow_Hours_Normalization * x72 + Aberdeen_Hours_Normalization * x73 + Belfast_Hours_Normalization * x74 + Manchester_Hours_Normalization * x75) <= (39240 - 4033), name ='Aircraft7 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x81 + Glasgow_Hours_Normalization * x82 + Aberdeen_Hours_Normalization * x83 + Belfast_Hours_Normalization * x84 + Manchester_Hours_Normalization * x85) <= (39240 - 4033), name ='Aircraft8 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x91 + Glasgow_Hours_Normalization * x92 + Aberdeen_Hours_Normalization * x93 + Belfast_Hours_Normalization * x94 + Manchester_Hours_Normalization * x95) <= (39240 - 4033), name ='Aircraft9 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x101 + Glasgow_Hours_Normalization * x102 + Aberdeen_Hours_Normalization * x103 + Belfast_Hours_Normalization * x104 + Manchester_Hours_Normalization * x105) <= (39240 - 4033), name ='Aircraft10 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x111 + Glasgow_Hours_Normalization * x112 + Aberdeen_Hours_Normalization * x113 + Belfast_Hours_Normalization * x114 + Manchester_Hours_Normalization * x115) <= (39240 - 4033), name ='Aircraft11 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x121 + Glasgow_Hours_Normalization * x122 + Aberdeen_Hours_Normalization * x123 + Belfast_Hours_Normalization * x124 + Manchester_Hours_Normalization * x125) <= (39240 - 4033), name ='Aircraft12 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x131 + Glasgow_Hours_Normalization * x132 + Aberdeen_Hours_Normalization * x133 + Belfast_Hours_Normalization * x134 + Manchester_Hours_Normalization * x135) <= (39240 - 4033), name ='Aircraft13 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x141 + Glasgow_Hours_Normalization * x142 + Aberdeen_Hours_Normalization * x143 + Belfast_Hours_Normalization * x144 + Manchester_Hours_Normalization * x145) <= (39240 - 4033), name ='Aircraft14 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x151 + Glasgow_Hours_Normalization * x152 + Aberdeen_Hours_Normalization * x153 + Belfast_Hours_Normalization * x154 + Manchester_Hours_Normalization * x155) <= (39240 - 4033), name ='Aircraft15 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x161 + Glasgow_Hours_Normalization * x162 + Aberdeen_Hours_Normalization * x163 + Belfast_Hours_Normalization * x164 + Manchester_Hours_Normalization * x165) <= (39240 - 4033), name ='Aircraft16 Operation Time Constraint')
MODEL.addConstr(2*(Edinburgh_Hours_Normalization * x171 + Glasgow_Hours_Normalization * x172 + Aberdeen_Hours_Normalization * x173 + Belfast_Hours_Normalization * x174 + Manchester_Hours_Normalization * x175) <= (39240 - 4033), name ='Aircraft17 Operation Time Constraint')

# Optimization Result Visualization
MODEL.optimize()

# Output Schedule Table
GetVariables = MODEL.getAttr('x')
VarsRef = np.reshape(GetVariables, [17,5])
Table = pd.DataFrame(VarsRef)
Table.columns = ['Edinburgh','Glasgow','Aberdeen','Belfast','Manchester']
Table.index = ['Aircraft1(A319)', 'Aircraft2(A319)', 'Aircraft3(A319)', 'Aircraft4(A319)', 'Aircraft5(A319)', 'Aircraft6(A320)', 'Aircraft7(A320)', 'Aircraft8(A320)', 'Aircraft9(A320)', 'Aircraft10(A320)', 'Aircraft11(A320)', 'Aircraft12(A320)', 'Aircraft13(A320)', 'Aircraft14(A320)','Aircraft15(A321)','Aircraft16(A321)','Aircraft17(A321)']
print(Table)

# for var in MODEL.getVars():
   # print(f"{var.varName}: {round(var.X, 3)}")

print("Optimal Objective Value:", MODEL.objVal)

A319_PartsCost = A319_PartCosts_Percentage * A319_Cost_Per_Hour * (Edinburgh_Hours_Normalization * sum(Table.iloc[0:5,0]) + Glasgow_Hours_Normalization * sum(Table.iloc[0:5,1]) + Aberdeen_Hours_Normalization * sum(Table.iloc[0:5,2]) + Belfast_Hours_Normalization * sum(Table.iloc[0:5,3]) + Manchester_Hours_Normalization * sum(Table.iloc[0:5,4]))
A320_PartsCost = A320_PartCosts_Percentage * A320_Cost_Per_Hour * (Edinburgh_Hours_Normalization * sum(Table.iloc[5:14,0]) + Glasgow_Hours_Normalization * sum(Table.iloc[5:14,1]) + Aberdeen_Hours_Normalization * sum(Table.iloc[5:14,2]) + Belfast_Hours_Normalization * sum(Table.iloc[5:14,3]) + Manchester_Hours_Normalization * sum(Table.iloc[5:14,4]))
A321_PartsCost = A321_PartCosts_Percentage * A321_Cost_Per_Hour * (Edinburgh_Hours_Normalization * sum(Table.iloc[14:17,0]) + Glasgow_Hours_Normalization * sum(Table.iloc[14:17,1]) + Aberdeen_Hours_Normalization * sum(Table.iloc[14:17,2]) + Belfast_Hours_Normalization * sum(Table.iloc[14:17,3]) + Manchester_Hours_Normalization * sum(Table.iloc[14:17,4]))
Total_PartCost = A319_PartsCost + A320_PartsCost + A321_PartsCost
print("Total Parts Cost:", Total_PartCost)

Total_U_A319 = 2*(Edinburgh_Hours_Normalization * sum(Table.iloc[0:5,0]) + Glasgow_Hours_Normalization * sum(Table.iloc[0:5,1]) + Aberdeen_Hours_Normalization * sum(Table.iloc[0:5,2]) + Belfast_Hours_Normalization * sum(Table.iloc[0:5,3]) + Manchester_Hours_Normalization * sum(Table.iloc[0:5,4]))/(5*(39240 - 4033))
Total_U_A320 = 2*(Edinburgh_Hours_Normalization * sum(Table.iloc[5:14,0]) + Glasgow_Hours_Normalization * sum(Table.iloc[5:14,1]) + Aberdeen_Hours_Normalization * sum(Table.iloc[5:14,2]) + Belfast_Hours_Normalization * sum(Table.iloc[5:14,3]) + Manchester_Hours_Normalization * sum(Table.iloc[5:14,4]))/(9*(39240 - 4033))
Total_U_A321 = 2*(Edinburgh_Hours_Normalization * sum(Table.iloc[14:17,0]) + Glasgow_Hours_Normalization * sum(Table.iloc[14:17,1]) + Aberdeen_Hours_Normalization * sum(Table.iloc[14:17,2]) + Belfast_Hours_Normalization * sum(Table.iloc[14:17,3]) + Manchester_Hours_Normalization * sum(Table.iloc[14:17,4]))/(3*(39240 - 4033))
A319_Percentage = "%.2f%%" % (Total_U_A319 * 100)
A320_Percentage = "%.2f%%" % (Total_U_A320 * 100)
A321_Percentage = "%.2f%%" % (Total_U_A321 * 100)
print("Total Utilization Rate of A319:",A319_Percentage)
print("Total Utilization Rate of A320:",A320_Percentage)
print("Total Utilization Rate of A321:",A321_Percentage)


# Visualization of optimization result
Table.plot.barh(title='Optimization Result',stacked='True')
