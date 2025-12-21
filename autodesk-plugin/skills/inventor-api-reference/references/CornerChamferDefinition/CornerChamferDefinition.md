# CornerChamferDefinition Object

## Description

The CornerChamferDefinition object is a utility object used for creating, querying, and editing sheet metal corner chamfer features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../CornerChamferDefinition/CornerChamferDefinition_Copy.md) | Function that creates a copy of this CornerChamferDefinition object. The copy is independent of any other object and can be edited without affecting anything else. It can then be used as input to either modify an existing corner round or create a new corner round feature. |
| [SetDistance](../CornerChamferDefinition/CornerChamferDefinition_SetDistance.md) | Method that changes the way this corner chamfer is defined so that it is defined using an equal distance from the corner. |
| [SetDistanceAndAngle](../CornerChamferDefinition/CornerChamferDefinition_SetDistanceAndAngle.md) | Method that changes the CornerChamferDefinition object to define a chamfer that is measured by an offset from the corner along one face and then ang chamfer feature where the chamfer is defined by a distance from an edge and an angle from a face. |
| [SetTwoDistances](../CornerChamferDefinition/CornerChamferDefinition_SetTwoDistances.md) | Method that changes the CornerChamferDefinition object to define a chamfer that is measured by two offset distances. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CornerChamferDefinition/CornerChamferDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ChamferDefinition](../CornerChamferDefinition/CornerChamferDefinition_ChamferDefinition.md) | Property that returns the ChamferDefinition object that defines how the chamfer is defined. |
| [ChamferDefinitionType](../CornerChamferDefinition/CornerChamferDefinition_ChamferDefinitionType.md) | Property that returns an enum indicating how the chamfer is defined. |
| [CornerEdges](../CornerChamferDefinition/CornerChamferDefinition_CornerEdges.md) | Gets the edges used for this corner chamfer. |
| [Parent](../CornerChamferDefinition/CornerChamferDefinition_Parent.md) | Property that returns the parent CornerChamferFeature object of this CornerChamferDefinition object. |
| [Type](../CornerChamferDefinition/CornerChamferDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CornerChamferDefinition.Copy](../CornerChamferDefinition/CornerChamferDefinition_Copy.md), [CornerChamferFeature.Definition](../CornerChamferFeature/CornerChamferFeature_Definition.md), [CornerChamferFeatureProxy.Definition](../CornerChamferFeatureProxy/CornerChamferFeatureProxy_Definition.md), [CornerChamferFeatures.CreateCornerChamferDefinition](../CornerChamferFeatures/CornerChamferFeatures_CreateCornerChamferDefinition.md)

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |