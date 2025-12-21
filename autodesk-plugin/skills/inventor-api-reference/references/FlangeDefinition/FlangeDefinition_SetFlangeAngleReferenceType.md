# FlangeDefinition.SetFlangeAngleReferenceType Method

Parent Object: [FlangeDefinition](../FlangeDefinition/FlangeDefinition.md)

## Description

Method that removes the override width extent for the specified physical flange.

## Syntax

FlangeDefinition.**SetFlangeAngleReferenceType**( ***ReferenceType*** As [FlangeReferenceTypeEnum](../FlangeReferenceTypeEnum.md), [***FlangeAngleOrReferencePlane***] As Variant, [***PlancementType***] As Variant )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ReferenceType | [FlangeReferenceTypeEnum](../FlangeReferenceTypeEnum.md) | Input FlangeReferenceTypeEnum that specifies which reference type to apply to the flange feature. |
| FlangeAngleOrReferencePlane | Variant | Optional input value to specify the flange angle or object to specify the reference plane. When the ReferenceType is speficied for flange angle, this can be a Double to indicate the radian value of the flange angle, or a String to indicate the flange angle as expression(like “135 deg”). When the ReferenceType is specified as kReferenceSelectedFaceOrWorkPlane then a Face or WorkPlance should be specified here as the reference plane. |
| PlancementType | Variant | Optional input DirectionEnum to specify the flange placement type. If this is not provided the kOutwardDirection is the default value for this argument, while the kInwardDirection is the flipped direction for the placement.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |