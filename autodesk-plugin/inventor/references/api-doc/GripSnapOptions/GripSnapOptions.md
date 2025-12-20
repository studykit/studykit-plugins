# GripSnapOptions Object

## Description

The GripSnapOptions object provides access to various grip snap related application level options. This object is obtained from the GeneralOptions.GripSnapOptions property.

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../GripSnapOptions/GripSnapOptions_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [DisplayObjectInOriginalLocation](../GripSnapOptions/GripSnapOptions_DisplayObjectInOriginalLocation.md) | Gets and sets whether or not to maintain a static reference image of the selection set while transient graphics represent the translation or rotation in drag and snap and reference geometry workflows. |
| [SelectGroundedComponentsAndWorkGeometry](../GripSnapOptions/GripSnapOptions_SelectGroundedComponentsAndWorkGeometry.md) | Gets and sets whether grounded components and work geometries can be included for move/rotate. |
| [ShowDegreesOfFreedom](../GripSnapOptions/GripSnapOptions_ShowDegreesOfFreedom.md) | Gets and sets whether or not to add boxes to the end of the heads-up display (HUD) for translational and rotational degrees of freedom related to the active component or assembly selection. |
| [Type](../GripSnapOptions/GripSnapOptions_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseFreeDrag](../GripSnapOptions/GripSnapOptions_UseFreeDrag.md) | Gets and sets whether or not to use the free drag option for each geometry type, skipping the step to select Free Drag from the Grip Snap move options. |
| [UseTemporaryConstraints](../GripSnapOptions/GripSnapOptions_UseTemporaryConstraints.md) | Gets and sets whether or not to use transient constraints during multiple manipulations of the same selection set. |

## Accessed From

[GeneralOptions.GripSnapOptions](../GeneralOptions/GeneralOptions_GripSnapOptions.md)

## Version

Introduced in version 2010

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |