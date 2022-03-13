// Find

PyModule_AddIntConstant(poModule, "CAMERA_STOP",			CPythonApplication::CAMERA_STOP);

// Add below

#ifdef ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM
	PyModule_AddIntConstant(poModule, "ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM", 1);
#else
	PyModule_AddIntConstant(poModule, "ENABLE_FATIH_SAHIN_LOTTERY_SYSTEM", 0);
#endif