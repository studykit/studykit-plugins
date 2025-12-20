# RibFeatures.CreateDefinition Method

Parent Object: [RibFeatures](../RibFeatures/RibFeatures.md)

## Description

Method that creates a new RibDefinition object. The object created does not represent a rib feature but instead is a representation of the information that defines a rib feature. You can use this object as input to the RibFeatures.Add method to create the actual feature.

## Remarks

The RibDefinition object returned is fully defined and can be used to create a rib feature. However, defaults are used for various options, so you may want to change some of the property values of the RibDefinition object before using it to create a feature.

## Syntax

RibFeatures.**CreateDefinition**( ***ProfileCurves*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***IsRib*** As Boolean, ***DirectionReversed*** As Boolean, ***Thickness*** As Variant ) As [RibDefinition](../RibDefinition/RibDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ProfileCurves | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection containing the sketch entities that will form the profile of the feature. |
| IsRib | Boolean | Input Boolean that specifies whether the sketch profile is projected lateral to the sketch plane (rib) or normal to the sketch plane (web) to create the feature. A value of True indicates that the profile is projected lateral to the sketch plane. |
| DirectionReversed | Boolean | Input Boolean that specifies whether the direction of the profile projection should be reversed. If the profile is projected normal to the sketch plane, setting this property to True causes the profile to be projected in the reverse direction of the sketch normal. If the profile is projected lateral to the sketch plane, setting this property to True causes the profile to be projected in the reverse direction of the natural normal direction of the base sketch entity. The natural normal of a sketch entity is defined as the cross-product of the vector representing the tangent at that point and the vector representing the sketch normal. |
| Thickness | Variant | Input Variant that defines the thickness of the rib feature. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document. |

## Version

Introduced in version 2012

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |