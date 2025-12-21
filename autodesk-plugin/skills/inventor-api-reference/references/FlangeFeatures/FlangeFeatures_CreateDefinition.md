# FlangeFeatures.CreateDefinition Method

Parent Object: [FlangeFeatures](../FlangeFeatures/FlangeFeatures.md)

## Description

Method that creates a new FlangeDefinition object. The object created does not represent a flange feature but instead is a representation of the information that defines a flange feature. You can use this object as input to the FlangeFeatures.Add method to cr.

## Syntax

FlangeFeatures.**CreateDefinition**( ***Edges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md), ***FlangeAngleReferenceType*** As [FlangeReferenceTypeEnum](../FlangeReferenceTypeEnum.md), ***FlangeAngleOrFlangeAngleReferencePlane*** As Variant, [***FlangePlacementType***] As Variant, [***Distance***] As Variant, [***Options***] As Variant ) As [FlangeDefinition](../FlangeDefinition/FlangeDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input EdgeCollection containing Edge objects used to create the flange feature. These Edge objects are in the first edge set for flange feature, the newly created FlangeDefinition can be used to add more FlangeEdgeSet objects. The FlangeEdgeSet object provides functions to set the width extent type, if not changed default kWidthEdgeExtent will be applied for it. |
| FlangeAngleReferenceType | [FlangeReferenceTypeEnum](../FlangeReferenceTypeEnum.md) | Input FlangeReferenceTypeEnum that defines the flange angle reference type. |
| FlangeAngleOrFlangeAngleReferencePlane | Variant | Input Variant that defines the angle of the flange. When the FlangeAngleReferenceType is set to kReferencePlaneThroughPartnerEdge, kReferencePlaneThroughSelectedEdge or kReferencePlaneAtSideFace, this can be a numeric value or a string to specify the flange angle value. When the FlangeAngleReferenceType is set to kReferenceSelectedFaceOrWorkPlane, this can be a WorkPlane or a Face to specify the flange angle reference plane. If a string or a numeric value is input, a parameter for this value will be created and the supplied string or numeric value is assigned to the parameter. If a numeric value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. If a WorkPlane or Face is input, the WorkPlane or Face should be parallel to the flange edge. |
| FlangePlacementType | Variant | Optional input DirectionEnum that defines the flange placement type. If not provided the default kOutwardDirection is used. |
| Distance | Variant | Optional input Variant that defines the distance used for the height extent of the flange. When the FlangeDefinition object is created it defaults to a distance height extent. This value is used to define that distance. If you want to define the height using a “to” extent instead you can edit the definition and change it, but to initially create the definition you must still supply an value for the distance.     This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. If not provided a default value will be used.   This is an optional argument whose default value is null. |
| Options | Variant | Optional input NameValueMap to specify more options. This is reserved for future use.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |