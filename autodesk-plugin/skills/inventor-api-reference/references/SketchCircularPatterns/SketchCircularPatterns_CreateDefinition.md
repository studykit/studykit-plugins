# SketchCircularPatterns.CreateDefinition Method

Parent Object: [SketchCircularPatterns](../SketchCircularPatterns/SketchCircularPatterns.md)

## Description

Creates a new sketch circular pattern definition. The new SketchCircularPatternDefinition object is returned.

## Syntax

SketchCircularPatterns.**CreateDefinition**( ***Geometries*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***AxisEntity*** As Object, [***NaturalAxisDirection***] As Variant, [***Count***] As Variant, [***Angle***] As Variant, [***Symmetric***] As Variant, [***Associative***] As Variant, [***Fitted***] As Variant, [***SuppressedElements***] As Variant, [***Reserved***] As Variant ) As [SketchCircularPatternDefinition](../SketchCircularPatternDefinition/SketchCircularPatternDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometries | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that contains the sketch geometries to be patterned. The collection could contain the various sketch entities and sketch blocks. When a SketchEntity has containing SketchBlock the SketchBlock should be used as input. The TextBox can’t be included in this argument but it can be included in a containing SketchBlock. |
| AxisEntity | Object | Input sketch entity that defines the axis entity. This can be a SketchPoint, SketchArc or SketchCircle. |
| NaturalAxisDirection | Variant | Optional input Boolean that indicates if the direction of the pattern is in the natural direction of the AxisEntity or reversed. A value of True indicates it is in the natural direction. If not provided this default to True. |
| Count | Variant | Optional input Variant that defines the number of instances in the x direction. This can be either a numeric value or a string. A parameter will be created to control this value when the pattern is created. If a string is input it can be any string that can be evaluated by Inventor to result in a unitless number(e.g. the name of a unitless Parameter).   This is an optional argument whose default value is null. |
| Angle | Variant | Optional input String or value to specify the angle between instances. A parameter will be created to control angle between instances when the pattern is created. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document, or it can be a name of an angular parameter.   This is an optional argument whose default value is null. |
| Symmetric | Variant | Optional input Boolean that specifies whether the occurrences are distributed on both sides of the original geometry. A value of True indicates the occurrences are distributed on both sides of the original geometry. If not provided this defaults to False.   This is an optional argument whose default value is null. |
| Associative | Variant | Optional input Boolean that specifies whether the pattern will update when changes are made to the part. If set this to False then the pattern constraints will be removed and the pattern will not update when change an element. If not provided this defaults to True.   This is an optional argument whose default value is null. |
| Fitted | Variant | Optional input Boolean that specifies whether pattern elements are equally fitted within the specified angle. If set to False, the pattern spacing measures the distance between elements instead of the overall angle for the pattern. If not provided this defaults to True.   This is an optional argument whose default value is null. |
| SuppressedElements | Variant | Optional input Long array that specifies the indices of the elements to be suppressed.   This is an optional argument whose default value is null. |
| Reserved | Variant | Reserved for future use.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025.1
