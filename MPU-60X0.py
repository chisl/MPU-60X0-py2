#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""MPU-60X0: MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS Motion Tracking Devices"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["InvenseSense"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from MPU_60X0_constants import *

# name:        MPU-60X0
# description: MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS Motion Tracking Devices
# manuf:       InvenseSense
# version:     0.1
# url:         https://store.invensense.com/datasheets/invensense/MPU-6050_DataSheet_V3%204.pdf
# date:        2016-08-01


# Derive from this class and implement read and write
class MPU_60X0_Base:
	"""MPU-6050 Six-Axis (Gyro + Accelerometer) MEMS Motion Tracking Devices"""
	# Register SELF_TEST_X
	
	
	def setSELF_TEST_X(self, val):
		"""Set register SELF_TEST_X"""
		self.write(REG.SELF_TEST_X, val, 8)
	
	def getSELF_TEST_X(self):
		"""Get register SELF_TEST_X"""
		return self.read(REG.SELF_TEST_X, 8)
	
	# Bits XA_TEST
	# Bits XG_TEST
	# Register SELF_TEST_Y
	
	
	def setSELF_TEST_Y(self, val):
		"""Set register SELF_TEST_Y"""
		self.write(REG.SELF_TEST_Y, val, 8)
	
	def getSELF_TEST_Y(self):
		"""Get register SELF_TEST_Y"""
		return self.read(REG.SELF_TEST_Y, 8)
	
	# Bits YA_TEST
	# Bits YG_TEST
	# Register SELF_TEST_Z
	
	
	def setSELF_TEST_Z(self, val):
		"""Set register SELF_TEST_Z"""
		self.write(REG.SELF_TEST_Z, val, 8)
	
	def getSELF_TEST_Z(self):
		"""Get register SELF_TEST_Z"""
		return self.read(REG.SELF_TEST_Z, 8)
	
	# Bits YA_TEST
	# Bits YG_TEST
	# Register SELF_TEST_A
	
	
	def setSELF_TEST_A(self, val):
		"""Set register SELF_TEST_A"""
		self.write(REG.SELF_TEST_A, val, 8)
	
	def getSELF_TEST_A(self):
		"""Get register SELF_TEST_A"""
		return self.read(REG.SELF_TEST_A, 8)
	
	# Bits RESERVED_0
	# Bits XA_TEST
	# Bits YA_TEST
	# Bits ZA_TEST
	# Register SMPLRT_DIV
	# Specify the divider from the gyroscope output rate used to generate the Sample Rate for the MPU-60X0.<br>
	#       Sample Rate = Gyroscope Output Rate / (1 + SMPLRT_DIV)<br>
	#       where Gyroscope Output Rate = 8kHz when the DLPF is disabled (DLPF_CFG = 0 or 7), and 1kHz when the DLPF is
	#       enabled (see Register 26). 
	
	
	def setSMPLRT_DIV(self, val):
		"""Set register SMPLRT_DIV"""
		self.write(REG.SMPLRT_DIV, val, 8)
	
	def getSMPLRT_DIV(self):
		"""Get register SMPLRT_DIV"""
		return self.read(REG.SMPLRT_DIV, 8)
	
	# Bits SMPLRT_DIV
	# Register CONFIG
	# This register configures the external Frame Synchronization (FSYNC) pin sampling and
	#       the Digital Low Pass Filter (DLPF) setting for both the gyroscopes and accelerometers. 
	
	
	def setCONFIG(self, val):
		"""Set register CONFIG"""
		self.write(REG.CONFIG, val, 8)
	
	def getCONFIG(self):
		"""Get register CONFIG"""
		return self.read(REG.CONFIG, 8)
	
	# Bits unused_0
	# Bits EXT_SYNC_SET
	# An external signal connected to the FSYNC pin can be sampled by configuring EXT_SYNC_SET.<br>
	#           Signal changes to the FSYNC pin are latched so that short strobes may be captured. The latched FSYNC signal will be sampled at the Sampling Rate, as defined in register 25. After sampling, the latch will reset to the current FSYNC signal state.<br>
	#           The sampled value will be reported in place of the least significant bit in a sensor data register determined by the value of EXT_SYNC_SET according to the following table. 
	
	# Bits DLPF_CFG
	# Accelerometer: Bandwidth/Hz Delay/ms; Gyro: Bandwidth/Hz Delay/ms Fs/kHz 
	# Register GYRO_CONFIG
	
	
	def setGYRO_CONFIG(self, val):
		"""Set register GYRO_CONFIG"""
		self.write(REG.GYRO_CONFIG, val, 8)
	
	def getGYRO_CONFIG(self):
		"""Get register GYRO_CONFIG"""
		return self.read(REG.GYRO_CONFIG, 8)
	
	# Bits unused_0
	# Bits FS_SEL
	# Bits unused_1
	# Register ACCEL_CONFIG
	
	
	def setACCEL_CONFIG(self, val):
		"""Set register ACCEL_CONFIG"""
		self.write(REG.ACCEL_CONFIG, val, 8)
	
	def getACCEL_CONFIG(self):
		"""Get register ACCEL_CONFIG"""
		return self.read(REG.ACCEL_CONFIG, 8)
	
	# Bits XA_ST
	# Bits YA_ST
	# Bits ZA_ST
	# Bits AFS_SEL
	# Bits unused_0
	# Register MOT_THR
	
	
	def setMOT_THR(self, val):
		"""Set register MOT_THR"""
		self.write(REG.MOT_THR, val, 8)
	
	def getMOT_THR(self):
		"""Get register MOT_THR"""
		return self.read(REG.MOT_THR, 8)
	
	# Bits MOT_THR
	# Register FIFO_EN
	
	
	def setFIFO_EN(self, val):
		"""Set register FIFO_EN"""
		self.write(REG.FIFO_EN, val, 8)
	
	def getFIFO_EN(self):
		"""Get register FIFO_EN"""
		return self.read(REG.FIFO_EN, 8)
	
	# Bits TEMP
	# Bits XG
	# Bits YG
	# Bits ZG
	# Bits ACCEL
	# Bits SLV2
	# Bits SLV1
	# Bits SLV0
	# Register I2C_MST_CTRL
	
	
	def setI2C_MST_CTRL(self, val):
		"""Set register I2C_MST_CTRL"""
		self.write(REG.I2C_MST_CTRL, val, 8)
	
	def getI2C_MST_CTRL(self):
		"""Get register I2C_MST_CTRL"""
		return self.read(REG.I2C_MST_CTRL, 8)
	
	# Bits MULT_MST_EN
	# Bits WAIT_FOR_ES
	# Bits SLV_3_FIFO_EN
	# Bits I2C_MST_P_NSR
	# Bits I2C_MST_CLK
	# Register I2C_SLV0_ADDR
	
	
	def setI2C_SLV0_ADDR(self, val):
		"""Set register I2C_SLV0_ADDR"""
		self.write(REG.I2C_SLV0_ADDR, val, 8)
	
	def getI2C_SLV0_ADDR(self):
		"""Get register I2C_SLV0_ADDR"""
		return self.read(REG.I2C_SLV0_ADDR, 8)
	
	# Bits I2C_SLV0_RW
	# Bits I2C_SLV0_ADDR
	# Register I2C_SLV0_REG
	
	
	def setI2C_SLV0_REG(self, val):
		"""Set register I2C_SLV0_REG"""
		self.write(REG.I2C_SLV0_REG, val, 8)
	
	def getI2C_SLV0_REG(self):
		"""Get register I2C_SLV0_REG"""
		return self.read(REG.I2C_SLV0_REG, 8)
	
	# Bits I2C_SLV0_REG
	# Register I2C_SLV0_CTRL
	
	
	def setI2C_SLV0_CTRL(self, val):
		"""Set register I2C_SLV0_CTRL"""
		self.write(REG.I2C_SLV0_CTRL, val, 8)
	
	def getI2C_SLV0_CTRL(self):
		"""Get register I2C_SLV0_CTRL"""
		return self.read(REG.I2C_SLV0_CTRL, 8)
	
	# Bits I2C_SLV0_EN
	# Bits I2C_SLV0_BYTE_SW
	# Bits I2C_SLV0_REG_DIS
	# Bits I2C_SLV0_GRP
	# Bits I2C_SLV0_LEN
	# Register I2C_SLV1_ADDR
	
	
	def setI2C_SLV1_ADDR(self, val):
		"""Set register I2C_SLV1_ADDR"""
		self.write(REG.I2C_SLV1_ADDR, val, 8)
	
	def getI2C_SLV1_ADDR(self):
		"""Get register I2C_SLV1_ADDR"""
		return self.read(REG.I2C_SLV1_ADDR, 8)
	
	# Bits I2C_SLV1_RW
	# Bits I2C_SLV1_ADDR
	# Register I2C_SLV1_REG
	
	
	def setI2C_SLV1_REG(self, val):
		"""Set register I2C_SLV1_REG"""
		self.write(REG.I2C_SLV1_REG, val, 8)
	
	def getI2C_SLV1_REG(self):
		"""Get register I2C_SLV1_REG"""
		return self.read(REG.I2C_SLV1_REG, 8)
	
	# Bits I2C_SLV1_REG
	# Register I2C_SLV1_CTRL
	
	
	def setI2C_SLV1_CTRL(self, val):
		"""Set register I2C_SLV1_CTRL"""
		self.write(REG.I2C_SLV1_CTRL, val, 8)
	
	def getI2C_SLV1_CTRL(self):
		"""Get register I2C_SLV1_CTRL"""
		return self.read(REG.I2C_SLV1_CTRL, 8)
	
	# Bits I2C_SLV1_EN
	# Bits I2C_SLV1_BYTE_SW
	# Bits I2C_SLV1_REG_DIS
	# Bits I2C_SLV1_GRP
	# Bits I2C_SLV1_LEN
	# Register I2C_SLV2_ADDR
	
	
	def setI2C_SLV2_ADDR(self, val):
		"""Set register I2C_SLV2_ADDR"""
		self.write(REG.I2C_SLV2_ADDR, val, 8)
	
	def getI2C_SLV2_ADDR(self):
		"""Get register I2C_SLV2_ADDR"""
		return self.read(REG.I2C_SLV2_ADDR, 8)
	
	# Bits I2C_SLV2_RW
	# Bits I2C_SLV2_ADDR
	# Register I2C_SLV2_REG
	
	
	def setI2C_SLV2_REG(self, val):
		"""Set register I2C_SLV2_REG"""
		self.write(REG.I2C_SLV2_REG, val, 8)
	
	def getI2C_SLV2_REG(self):
		"""Get register I2C_SLV2_REG"""
		return self.read(REG.I2C_SLV2_REG, 8)
	
	# Bits I2C_SLV2_REG
	# Register I2C_SLV2_CTRL
	
	
	def setI2C_SLV2_CTRL(self, val):
		"""Set register I2C_SLV2_CTRL"""
		self.write(REG.I2C_SLV2_CTRL, val, 8)
	
	def getI2C_SLV2_CTRL(self):
		"""Get register I2C_SLV2_CTRL"""
		return self.read(REG.I2C_SLV2_CTRL, 8)
	
	# Bits I2C_SLV2_EN
	# Bits I2C_SLV2_BYTE_SW
	# Bits I2C_SLV2_REG_DIS
	# Bits I2C_SLV2_GRP
	# Bits I2C_SLV2_LEN
	# Register I2C_SLV3_ADDR
	
	
	def setI2C_SLV3_ADDR(self, val):
		"""Set register I2C_SLV3_ADDR"""
		self.write(REG.I2C_SLV3_ADDR, val, 8)
	
	def getI2C_SLV3_ADDR(self):
		"""Get register I2C_SLV3_ADDR"""
		return self.read(REG.I2C_SLV3_ADDR, 8)
	
	# Bits I2C_SLV3_RW
	# Bits I2C_SLV3_ADDR
	# Register I2C_SLV3_REG
	
	
	def setI2C_SLV3_REG(self, val):
		"""Set register I2C_SLV3_REG"""
		self.write(REG.I2C_SLV3_REG, val, 8)
	
	def getI2C_SLV3_REG(self):
		"""Get register I2C_SLV3_REG"""
		return self.read(REG.I2C_SLV3_REG, 8)
	
	# Bits I2C_SLV3_REG
	# Register I2C_SLV3_CTRL
	
	
	def setI2C_SLV3_CTRL(self, val):
		"""Set register I2C_SLV3_CTRL"""
		self.write(REG.I2C_SLV3_CTRL, val, 8)
	
	def getI2C_SLV3_CTRL(self):
		"""Get register I2C_SLV3_CTRL"""
		return self.read(REG.I2C_SLV3_CTRL, 8)
	
	# Bits I2C_SLV3_EN
	# Bits I2C_SLV3_BYTE_SW
	# Bits I2C_SLV3_REG_DIS
	# Bits I2C_SLV3_GRP
	# Bits I2C_SLV3_LEN
	# Register I2C_SLV4_ADDR
	
	
	def setI2C_SLV4_ADDR(self, val):
		"""Set register I2C_SLV4_ADDR"""
		self.write(REG.I2C_SLV4_ADDR, val, 8)
	
	def getI2C_SLV4_ADDR(self):
		"""Get register I2C_SLV4_ADDR"""
		return self.read(REG.I2C_SLV4_ADDR, 8)
	
	# Bits I2C_SLV4_RW
	# Bits I2C_SLV4_ADDR
	# Register I2C_SLV4_REG
	
	
	def setI2C_SLV4_REG(self, val):
		"""Set register I2C_SLV4_REG"""
		self.write(REG.I2C_SLV4_REG, val, 8)
	
	def getI2C_SLV4_REG(self):
		"""Get register I2C_SLV4_REG"""
		return self.read(REG.I2C_SLV4_REG, 8)
	
	# Bits I2C_SLV4_REG
	# Register I2C_SLV4_DO
	
	
	def setI2C_SLV4_DO(self, val):
		"""Set register I2C_SLV4_DO"""
		self.write(REG.I2C_SLV4_DO, val, 8)
	
	def getI2C_SLV4_DO(self):
		"""Get register I2C_SLV4_DO"""
		return self.read(REG.I2C_SLV4_DO, 8)
	
	# Bits I2C_SLV4_DO
	# Register I2C_SLV4_CTRL
	
	
	def setI2C_SLV4_CTRL(self, val):
		"""Set register I2C_SLV4_CTRL"""
		self.write(REG.I2C_SLV4_CTRL, val, 8)
	
	def getI2C_SLV4_CTRL(self):
		"""Get register I2C_SLV4_CTRL"""
		return self.read(REG.I2C_SLV4_CTRL, 8)
	
	# Bits I2C_SLV4_EN
	# Bits I2C_SLV4_INT_EN
	# Bits I2C_SLV4_REG_DIS
	# Bits I2C_MST_DLY
	# Register ACCEL_XOUT
	
	
	def setACCEL_XOUT(self, val):
		"""Set register ACCEL_XOUT"""
		self.write(REG.ACCEL_XOUT, val, 16)
	
	def getACCEL_XOUT(self):
		"""Get register ACCEL_XOUT"""
		return self.read(REG.ACCEL_XOUT, 16)
	
	# Bits ACCEL_XOUT
	# Register ACCEL_YOUT
	
	
	def setACCEL_YOUT(self, val):
		"""Set register ACCEL_YOUT"""
		self.write(REG.ACCEL_YOUT, val, 16)
	
	def getACCEL_YOUT(self):
		"""Get register ACCEL_YOUT"""
		return self.read(REG.ACCEL_YOUT, 16)
	
	# Bits ACCEL_YOUT
	# Register ACCEL_ZOUT
	
	
	def setACCEL_ZOUT(self, val):
		"""Set register ACCEL_ZOUT"""
		self.write(REG.ACCEL_ZOUT, val, 16)
	
	def getACCEL_ZOUT(self):
		"""Get register ACCEL_ZOUT"""
		return self.read(REG.ACCEL_ZOUT, 16)
	
	# Bits ACCEL_ZOUT
	# Register TEMP_OUT
	
	
	def setTEMP_OUT(self, val):
		"""Set register TEMP_OUT"""
		self.write(REG.TEMP_OUT, val, 16)
	
	def getTEMP_OUT(self):
		"""Get register TEMP_OUT"""
		return self.read(REG.TEMP_OUT, 16)
	
	# Bits TEMP_OUT
	# Register GYRO_XOUT
	
	
	def setGYRO_XOUT(self, val):
		"""Set register GYRO_XOUT"""
		self.write(REG.GYRO_XOUT, val, 16)
	
	def getGYRO_XOUT(self):
		"""Get register GYRO_XOUT"""
		return self.read(REG.GYRO_XOUT, 16)
	
	# Bits GYRO_XOUT
	# Register GYRO_YOUT
	
	
	def setGYRO_YOUT(self, val):
		"""Set register GYRO_YOUT"""
		self.write(REG.GYRO_YOUT, val, 16)
	
	def getGYRO_YOUT(self):
		"""Get register GYRO_YOUT"""
		return self.read(REG.GYRO_YOUT, 16)
	
	# Bits GYRO_YOUT
	# Register GYRO_ZOUT
	
	
	def setGYRO_ZOUT(self, val):
		"""Set register GYRO_ZOUT"""
		self.write(REG.GYRO_ZOUT, val, 16)
	
	def getGYRO_ZOUT(self):
		"""Get register GYRO_ZOUT"""
		return self.read(REG.GYRO_ZOUT, 16)
	
	# Bits GYRO_ZOUT
	# Register EXT_SENS_DATA_00
	
	
	def setEXT_SENS_DATA_00(self, val):
		"""Set register EXT_SENS_DATA_00"""
		self.write(REG.EXT_SENS_DATA_00, val, 8)
	
	def getEXT_SENS_DATA_00(self):
		"""Get register EXT_SENS_DATA_00"""
		return self.read(REG.EXT_SENS_DATA_00, 8)
	
	# Bits EXT_SENS_DATA_00
	# Register EXT_SENS_DATA_01
	
	
	def setEXT_SENS_DATA_01(self, val):
		"""Set register EXT_SENS_DATA_01"""
		self.write(REG.EXT_SENS_DATA_01, val, 8)
	
	def getEXT_SENS_DATA_01(self):
		"""Get register EXT_SENS_DATA_01"""
		return self.read(REG.EXT_SENS_DATA_01, 8)
	
	# Bits EXT_SENS_DATA_01
	# Register EXT_SENS_DATA_02
	
	
	def setEXT_SENS_DATA_02(self, val):
		"""Set register EXT_SENS_DATA_02"""
		self.write(REG.EXT_SENS_DATA_02, val, 8)
	
	def getEXT_SENS_DATA_02(self):
		"""Get register EXT_SENS_DATA_02"""
		return self.read(REG.EXT_SENS_DATA_02, 8)
	
	# Bits EXT_SENS_DATA_02
	# Register EXT_SENS_DATA_03
	
	
	def setEXT_SENS_DATA_03(self, val):
		"""Set register EXT_SENS_DATA_03"""
		self.write(REG.EXT_SENS_DATA_03, val, 8)
	
	def getEXT_SENS_DATA_03(self):
		"""Get register EXT_SENS_DATA_03"""
		return self.read(REG.EXT_SENS_DATA_03, 8)
	
	# Bits EXT_SENS_DATA_03
	# Register EXT_SENS_DATA_04
	
	
	def setEXT_SENS_DATA_04(self, val):
		"""Set register EXT_SENS_DATA_04"""
		self.write(REG.EXT_SENS_DATA_04, val, 8)
	
	def getEXT_SENS_DATA_04(self):
		"""Get register EXT_SENS_DATA_04"""
		return self.read(REG.EXT_SENS_DATA_04, 8)
	
	# Bits EXT_SENS_DATA_04
	# Register EXT_SENS_DATA_05
	
	
	def setEXT_SENS_DATA_05(self, val):
		"""Set register EXT_SENS_DATA_05"""
		self.write(REG.EXT_SENS_DATA_05, val, 8)
	
	def getEXT_SENS_DATA_05(self):
		"""Get register EXT_SENS_DATA_05"""
		return self.read(REG.EXT_SENS_DATA_05, 8)
	
	# Bits EXT_SENS_DATA_05
	# Register EXT_SENS_DATA_06
	
	
	def setEXT_SENS_DATA_06(self, val):
		"""Set register EXT_SENS_DATA_06"""
		self.write(REG.EXT_SENS_DATA_06, val, 8)
	
	def getEXT_SENS_DATA_06(self):
		"""Get register EXT_SENS_DATA_06"""
		return self.read(REG.EXT_SENS_DATA_06, 8)
	
	# Bits EXT_SENS_DATA_06
	# Register EXT_SENS_DATA_07
	
	
	def setEXT_SENS_DATA_07(self, val):
		"""Set register EXT_SENS_DATA_07"""
		self.write(REG.EXT_SENS_DATA_07, val, 8)
	
	def getEXT_SENS_DATA_07(self):
		"""Get register EXT_SENS_DATA_07"""
		return self.read(REG.EXT_SENS_DATA_07, 8)
	
	# Bits EXT_SENS_DATA_07
	# Register EXT_SENS_DATA_08
	
	
	def setEXT_SENS_DATA_08(self, val):
		"""Set register EXT_SENS_DATA_08"""
		self.write(REG.EXT_SENS_DATA_08, val, 8)
	
	def getEXT_SENS_DATA_08(self):
		"""Get register EXT_SENS_DATA_08"""
		return self.read(REG.EXT_SENS_DATA_08, 8)
	
	# Bits EXT_SENS_DATA_08
	# Register EXT_SENS_DATA_09
	
	
	def setEXT_SENS_DATA_09(self, val):
		"""Set register EXT_SENS_DATA_09"""
		self.write(REG.EXT_SENS_DATA_09, val, 8)
	
	def getEXT_SENS_DATA_09(self):
		"""Get register EXT_SENS_DATA_09"""
		return self.read(REG.EXT_SENS_DATA_09, 8)
	
	# Bits EXT_SENS_DATA_09
	# Register EXT_SENS_DATA_10
	
	
	def setEXT_SENS_DATA_10(self, val):
		"""Set register EXT_SENS_DATA_10"""
		self.write(REG.EXT_SENS_DATA_10, val, 8)
	
	def getEXT_SENS_DATA_10(self):
		"""Get register EXT_SENS_DATA_10"""
		return self.read(REG.EXT_SENS_DATA_10, 8)
	
	# Bits EXT_SENS_DATA_10
	# Register EXT_SENS_DATA_11
	
	
	def setEXT_SENS_DATA_11(self, val):
		"""Set register EXT_SENS_DATA_11"""
		self.write(REG.EXT_SENS_DATA_11, val, 8)
	
	def getEXT_SENS_DATA_11(self):
		"""Get register EXT_SENS_DATA_11"""
		return self.read(REG.EXT_SENS_DATA_11, 8)
	
	# Bits EXT_SENS_DATA_11
	# Register EXT_SENS_DATA_12
	
	
	def setEXT_SENS_DATA_12(self, val):
		"""Set register EXT_SENS_DATA_12"""
		self.write(REG.EXT_SENS_DATA_12, val, 8)
	
	def getEXT_SENS_DATA_12(self):
		"""Get register EXT_SENS_DATA_12"""
		return self.read(REG.EXT_SENS_DATA_12, 8)
	
	# Bits EXT_SENS_DATA_12
	# Register EXT_SENS_DATA_13
	
	
	def setEXT_SENS_DATA_13(self, val):
		"""Set register EXT_SENS_DATA_13"""
		self.write(REG.EXT_SENS_DATA_13, val, 8)
	
	def getEXT_SENS_DATA_13(self):
		"""Get register EXT_SENS_DATA_13"""
		return self.read(REG.EXT_SENS_DATA_13, 8)
	
	# Bits EXT_SENS_DATA_13
	# Register EXT_SENS_DATA_14
	
	
	def setEXT_SENS_DATA_14(self, val):
		"""Set register EXT_SENS_DATA_14"""
		self.write(REG.EXT_SENS_DATA_14, val, 8)
	
	def getEXT_SENS_DATA_14(self):
		"""Get register EXT_SENS_DATA_14"""
		return self.read(REG.EXT_SENS_DATA_14, 8)
	
	# Bits EXT_SENS_DATA_14
	# Register EXT_SENS_DATA_15
	
	
	def setEXT_SENS_DATA_15(self, val):
		"""Set register EXT_SENS_DATA_15"""
		self.write(REG.EXT_SENS_DATA_15, val, 8)
	
	def getEXT_SENS_DATA_15(self):
		"""Get register EXT_SENS_DATA_15"""
		return self.read(REG.EXT_SENS_DATA_15, 8)
	
	# Bits EXT_SENS_DATA_15
	# Register EXT_SENS_DATA_16
	
	
	def setEXT_SENS_DATA_16(self, val):
		"""Set register EXT_SENS_DATA_16"""
		self.write(REG.EXT_SENS_DATA_16, val, 8)
	
	def getEXT_SENS_DATA_16(self):
		"""Get register EXT_SENS_DATA_16"""
		return self.read(REG.EXT_SENS_DATA_16, 8)
	
	# Bits EXT_SENS_DATA_16
	# Register EXT_SENS_DATA_17
	
	
	def setEXT_SENS_DATA_17(self, val):
		"""Set register EXT_SENS_DATA_17"""
		self.write(REG.EXT_SENS_DATA_17, val, 8)
	
	def getEXT_SENS_DATA_17(self):
		"""Get register EXT_SENS_DATA_17"""
		return self.read(REG.EXT_SENS_DATA_17, 8)
	
	# Bits EXT_SENS_DATA_17
	# Register EXT_SENS_DATA_18
	
	
	def setEXT_SENS_DATA_18(self, val):
		"""Set register EXT_SENS_DATA_18"""
		self.write(REG.EXT_SENS_DATA_18, val, 8)
	
	def getEXT_SENS_DATA_18(self):
		"""Get register EXT_SENS_DATA_18"""
		return self.read(REG.EXT_SENS_DATA_18, 8)
	
	# Bits EXT_SENS_DATA_18
	# Register EXT_SENS_DATA_19
	
	
	def setEXT_SENS_DATA_19(self, val):
		"""Set register EXT_SENS_DATA_19"""
		self.write(REG.EXT_SENS_DATA_19, val, 8)
	
	def getEXT_SENS_DATA_19(self):
		"""Get register EXT_SENS_DATA_19"""
		return self.read(REG.EXT_SENS_DATA_19, 8)
	
	# Bits EXT_SENS_DATA_19
	# Register EXT_SENS_DATA_20
	
	
	def setEXT_SENS_DATA_20(self, val):
		"""Set register EXT_SENS_DATA_20"""
		self.write(REG.EXT_SENS_DATA_20, val, 8)
	
	def getEXT_SENS_DATA_20(self):
		"""Get register EXT_SENS_DATA_20"""
		return self.read(REG.EXT_SENS_DATA_20, 8)
	
	# Bits EXT_SENS_DATA_20
	# Register EXT_SENS_DATA_21
	
	
	def setEXT_SENS_DATA_21(self, val):
		"""Set register EXT_SENS_DATA_21"""
		self.write(REG.EXT_SENS_DATA_21, val, 8)
	
	def getEXT_SENS_DATA_21(self):
		"""Get register EXT_SENS_DATA_21"""
		return self.read(REG.EXT_SENS_DATA_21, 8)
	
	# Bits EXT_SENS_DATA_21
	# Register EXT_SENS_DATA_22
	
	
	def setEXT_SENS_DATA_22(self, val):
		"""Set register EXT_SENS_DATA_22"""
		self.write(REG.EXT_SENS_DATA_22, val, 8)
	
	def getEXT_SENS_DATA_22(self):
		"""Get register EXT_SENS_DATA_22"""
		return self.read(REG.EXT_SENS_DATA_22, 8)
	
	# Bits EXT_SENS_DATA_22
	# Register EXT_SENS_DATA_23
	
	
	def setEXT_SENS_DATA_23(self, val):
		"""Set register EXT_SENS_DATA_23"""
		self.write(REG.EXT_SENS_DATA_23, val, 8)
	
	def getEXT_SENS_DATA_23(self):
		"""Get register EXT_SENS_DATA_23"""
		return self.read(REG.EXT_SENS_DATA_23, 8)
	
	# Bits EXT_SENS_DATA_23
	# Register I2C_SLV0_DO
	
	
	def setI2C_SLV0_DO(self, val):
		"""Set register I2C_SLV0_DO"""
		self.write(REG.I2C_SLV0_DO, val, 8)
	
	def getI2C_SLV0_DO(self):
		"""Get register I2C_SLV0_DO"""
		return self.read(REG.I2C_SLV0_DO, 8)
	
	# Bits I2C_SLV0_DO
	# Register I2C_SLV1_DO
	
	
	def setI2C_SLV1_DO(self, val):
		"""Set register I2C_SLV1_DO"""
		self.write(REG.I2C_SLV1_DO, val, 8)
	
	def getI2C_SLV1_DO(self):
		"""Get register I2C_SLV1_DO"""
		return self.read(REG.I2C_SLV1_DO, 8)
	
	# Bits I2C_SLV1_DO
	# Register I2C_SLV2_DO
	
	
	def setI2C_SLV2_DO(self, val):
		"""Set register I2C_SLV2_DO"""
		self.write(REG.I2C_SLV2_DO, val, 8)
	
	def getI2C_SLV2_DO(self):
		"""Get register I2C_SLV2_DO"""
		return self.read(REG.I2C_SLV2_DO, 8)
	
	# Bits I2C_SLV2_DO
	# Register I2C_SLV3_DO
	
	
	def setI2C_SLV3_DO(self, val):
		"""Set register I2C_SLV3_DO"""
		self.write(REG.I2C_SLV3_DO, val, 8)
	
	def getI2C_SLV3_DO(self):
		"""Get register I2C_SLV3_DO"""
		return self.read(REG.I2C_SLV3_DO, 8)
	
	# Bits I2C_SLV3_DO
	# Register I2C_MST_DELAY_CTRL
	
	
	def setI2C_MST_DELAY_CTRL(self, val):
		"""Set register I2C_MST_DELAY_CTRL"""
		self.write(REG.I2C_MST_DELAY_CTRL, val, 8)
	
	def getI2C_MST_DELAY_CTRL(self):
		"""Get register I2C_MST_DELAY_CTRL"""
		return self.read(REG.I2C_MST_DELAY_CTRL, 8)
	
	# Bits DELAY_ES_SHADOW
	# Bits unused_0
	# Bits I2C_SLV4_DLY_EN
	# Bits I2C_SLV3_DLY_EN
	# Bits I2C_SLV2_DLY_EN
	# Bits I2C_SLV1_DLY_EN
	# Bits I2C_SLV0_DLY_EN
	# Register SIGNAL_PATH_RESET
	
	
	def setSIGNAL_PATH_RESET(self, val):
		"""Set register SIGNAL_PATH_RESET"""
		self.write(REG.SIGNAL_PATH_RESET, val, 8)
	
	def getSIGNAL_PATH_RESET(self):
		"""Get register SIGNAL_PATH_RESET"""
		return self.read(REG.SIGNAL_PATH_RESET, 8)
	
	# Bits unused_0
	# Bits GYRO_RESET
	# Bits ACCEL_RESET
	# Bits TEMP_RESET
	# Register MOT_DETECT_CTRL
	
	
	def setMOT_DETECT_CTRL(self, val):
		"""Set register MOT_DETECT_CTRL"""
		self.write(REG.MOT_DETECT_CTRL, val, 8)
	
	def getMOT_DETECT_CTRL(self):
		"""Get register MOT_DETECT_CTRL"""
		return self.read(REG.MOT_DETECT_CTRL, 8)
	
	# Bits unused_0
	# Bits ACCEL_ON_DELAY
	# Bits unused_1
	# Register USER_CTRL
	
	
	def setUSER_CTRL(self, val):
		"""Set register USER_CTRL"""
		self.write(REG.USER_CTRL, val, 8)
	
	def getUSER_CTRL(self):
		"""Get register USER_CTRL"""
		return self.read(REG.USER_CTRL, 8)
	
	# Bits unused_0
	# Bits FIFO_EN
	# Bits I2C_MST_EN
	# Bits I2C_IF_DIS
	# Bits unused_1
	# Bits FIFO_RESET
	# Bits I2C_MST_RESET
	# Bits SIG_COND_RESET
	# Register PWR_MGMT_1
	
	
	def setPWR_MGMT_1(self, val):
		"""Set register PWR_MGMT_1"""
		self.write(REG.PWR_MGMT_1, val, 8)
	
	def getPWR_MGMT_1(self):
		"""Get register PWR_MGMT_1"""
		return self.read(REG.PWR_MGMT_1, 8)
	
	# Bits DEVICE_RESET
	# Bits SLEEP
	# Bits CYCLE
	# Bits unused_0
	# Bits TEMP_DIS
	# Bits CLKSEL
	# Register PWR_MGMT_2
	
	
	def setPWR_MGMT_2(self, val):
		"""Set register PWR_MGMT_2"""
		self.write(REG.PWR_MGMT_2, val, 8)
	
	def getPWR_MGMT_2(self):
		"""Get register PWR_MGMT_2"""
		return self.read(REG.PWR_MGMT_2, 8)
	
	# Bits LP_WAKE_CTRL
	# Bits STBY_XA
	# Bits STBY_YA
	# Bits STBY_ZA
	# Bits STBY_XG
	# Bits STBY_YG
	# Bits STBY_ZG
	# Register FIFO_COUNT
	
	
	def setFIFO_COUNT(self, val):
		"""Set register FIFO_COUNT"""
		self.write(REG.FIFO_COUNT, val, 16)
	
	def getFIFO_COUNT(self):
		"""Get register FIFO_COUNT"""
		return self.read(REG.FIFO_COUNT, 16)
	
	# Bits FIFO_COUNT
	# Register FIFO_R_W
	
	
	def setFIFO_R_W(self, val):
		"""Set register FIFO_R_W"""
		self.write(REG.FIFO_R_W, val, 8)
	
	def getFIFO_R_W(self):
		"""Get register FIFO_R_W"""
		return self.read(REG.FIFO_R_W, 8)
	
	# Bits FIFO_R_W
	# Register WHO_AM_I
	
	
	def setWHO_AM_I(self, val):
		"""Set register WHO_AM_I"""
		self.write(REG.WHO_AM_I, val, 8)
	
	def getWHO_AM_I(self):
		"""Get register WHO_AM_I"""
		return self.read(REG.WHO_AM_I, 8)
	
	# Bits unused_0
	# Bits WhoAmI
