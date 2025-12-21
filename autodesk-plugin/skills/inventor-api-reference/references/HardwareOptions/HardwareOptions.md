# HardwareOptions Object

## Description

The HardwareOptions object provides access to properties that provide read and write access of the hardware related application options. This is somewhat equivalent to the Hardware tab of the Application Options dialog.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../HardwareOptions/HardwareOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Diagnostics](../HardwareOptions/HardwareOptions_Diagnostics.md) | Property that returns a string with results of diagnostic testing. |
| [EnableViewportGPURayTracing](../HardwareOptions/HardwareOptions_EnableViewportGPURayTracing.md) | Read-write property that specifies whether to use GPU Raytracing. |
| [GraphicsSettingType](../HardwareOptions/HardwareOptions_GraphicsSettingType.md) | Read-write property that specifies the type of the graphics hardware setting to use. |
| [Type](../HardwareOptions/HardwareOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseSoftwareGraphics](../HardwareOptions/HardwareOptions_UseSoftwareGraphics.md) | Read-write property that specifies whether to use software graphics. |

## Accessed From

[Application.HardwareOptions](../Application/Application_HardwareOptions.md), [ApprenticeServer.HardwareOptions](../ApprenticeServer/ApprenticeServer_HardwareOptions.md), [ApprenticeServerComponent.HardwareOptions](../ApprenticeServerComponent/ApprenticeServerComponent_HardwareOptions.md), [InventorServer.HardwareOptions](InventorServer_HardwareOptions.md), [InventorServerObject.HardwareOptions](InventorServerObject_HardwareOptions.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |