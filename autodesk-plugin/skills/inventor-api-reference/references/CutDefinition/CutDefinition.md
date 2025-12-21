# CutDefinition Object

## Description

The CutDefinition object represents all of the information that defines a cut feature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [SetCutAcrossBendsExtent](../CutDefinition/CutDefinition_SetCutAcrossBendsExtent.md) | Method that changes the cut to cut across bends. |
| [SetDistanceExtent](../CutDefinition/CutDefinition_SetDistanceExtent.md) | Method that changes the extent to be a distance extent. |
| [SetFromToExtent](../CutDefinition/CutDefinition_SetFromToExtent.md) | Method that changes the extent to be a 'from to' extent. |
| [SetThroughAllExtent](../CutDefinition/CutDefinition_SetThroughAllExtent.md) | Method that changes the extent to be a 'to next' extent. |
| [SetToExtent](../CutDefinition/CutDefinition_SetToExtent.md) | Method that changes the extent to be a 'to' extent. |
| [SetToNextExtent](../CutDefinition/CutDefinition_SetToNextExtent.md) | Method that changes the extent to be a 'to next' extent. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../CutDefinition/CutDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [CutAcrossBends](../CutDefinition/CutDefinition_CutAcrossBends.md) | Property that returns whether this cut feature goes across bends or not. |
| [CutNormalToFlat](../CutDefinition/CutDefinition_CutNormalToFlat.md) | Read-write property that gets and sets whether the side faces of this cut feature are perpendicular to the top/bottom faces of the flat. This simulates most manufacturing processes where the cut is made perpendicular to the sheet stock. |
| [Extent](../CutDefinition/CutDefinition_Extent.md) | Property that returns the PartFeatureExtent object that defines how the extent of the feature is defined. |
| [ExtentType](../CutDefinition/CutDefinition_ExtentType.md) | Property that returns an enum value indicating how the extent of the feature is defined. |
| [Parent](../CutDefinition/CutDefinition_Parent.md) | Property that returns the parent CutFeature object of this CutDefinition object. |
| [Profile](../CutDefinition/CutDefinition_Profile.md) | Gets the Profile object that defines the shape of the cut. |
| [Type](../CutDefinition/CutDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[CutFeature.Definition](../CutFeature/CutFeature_Definition.md), [CutFeatureProxy.Definition](../CutFeatureProxy/CutFeatureProxy_Definition.md), [CutFeatures.CreateCutDefinition](../CutFeatures/CutFeatures_CreateCutDefinition.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal face and cut features](../../sample-programs/SheetMetalFeatures_Sample.md) | This sample demonstrates the creation of sheet metal face and cut features. |

## Version

Introduced in version 2009

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |