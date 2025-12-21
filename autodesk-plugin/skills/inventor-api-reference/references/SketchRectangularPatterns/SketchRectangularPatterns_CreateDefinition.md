# SketchRectangularPatterns.CreateDefinition Method

Parent Object: [SketchRectangularPatterns](../SketchRectangularPatterns/SketchRectangularPatterns.md)

## Description

Creates a new sketch rectangular pattern definition. The new SketchRectangularPatternDefinition object is returned.

## Syntax

SketchRectangularPatterns.**CreateDefinition**( ***Geometries*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***XDirectionEntity*** As Object, ***XCount*** As Variant, [***NaturalXDirection***] As Variant, [***XDirectionSymmetric***] As Variant, [***XSpacing***] As Variant, [***YDirectionEntity***] As Variant, [***YCount***] As Variant, [***NaturalYDirection***] As Variant, [***YDirectionSymmetric***] As Variant, [***YSpacing***] As Variant, [***Associative***] As Variant, [***Fitted***] As Variant, [***SuppressedElements***] As Variant, [***Reserved***] As Variant ) As [SketchRectangularPatternDefinition](../SketchRectangularPatternDefinition/SketchRectangularPatternDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Geometries | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection object that contains the sketch geometries to be patterned. The collection could contain the various sketch entities and sketch blocks. When a SketchEntity has containing SketchBlock the SketchBlock should be used as input. The TextBox can’t be included in this argument but it can be included in a containing SketchBlock. |
| XDirectionEntity | Object | Input linear sketch entity that defines the X direction. |
| XCount | Variant | Input Variant that defines the number of instances in the x direction. This can be either a numeric value or a string. A parameter will be created to control this value when the pattern is created. If a string is input it can be any string that can be evaluated by Inventor to result in a unitless number(e.g. the name of a unitless Parameter). |
| NaturalXDirection | Variant | Optional input Boolean that indicates if the direction of the pattern is in the natural direction of the XDirectionEntity or reversed. A value of True indicates it is in the natural direction. If not provided this default to True. |
| XDirectionSymmetric | Variant | Optional input Boolean that indicates if the occurrences are distributed on both sides of the original geometry. If the occurrence count is even, NaturalXDirection can indicate which side gets the extra occurrence. A value of True indicates the occurrences are distributed on both sides of the original geometry. If not provided this default to False.   This is an optional argument whose default value is null. |
| XSpacing | Variant | Optional input String or value to specify the spacing between instances in the X direction. A parameter will be created to control spacing between instances in the X direction when the pattern is created. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document.   This is an optional argument whose default value is null. |
| YDirectionEntity | Variant | Optional input linear sketch entity that defines the Y direction.   This is an optional argument whose default value is null. |
| YCount | Variant | Optional input Variant that defines the number of instances in the Y direction. This can be either a numeric value or a string. A parameter will be created to control this value when the pattern is created. If a string is input it can be any string that can be evaluated by Inventor to result in a unitless number(e.g. the name of a unitless Parameter).   This is an optional argument whose default value is null. |
| NaturalYDirection | Variant | Optional input Boolean that indicates if the direction of the pattern is in the natural direction of the YDirectionEntity or reversed. A value of True indicates it is in the natural direction. If not provided this default to True.   This is an optional argument whose default value is null. |
| YDirectionSymmetric | Variant | Optional input Boolean that indicates if the occurrences are distributed on both sides of the original geometry. If the occurrence count is even, NaturalYDirection can indicate which side gets the extra occurrence. A value of True indicates the occurrences are distributed on both sides of the original geometry. If not provided this default to False.   This is an optional argument whose default value is null. |
| YSpacing | Variant | Optional input String or value to specify the spacing between instances in the Y direction. A parameter will be created to control spacing between instances in the Y direction when the pattern is created. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current length units of the document.   This is an optional argument whose default value is null. |
| Associative | Variant | Optional input Boolean that specifies whether the pattern will update when changes are made to the part. If set this to False then the pattern constraints will be removed and the pattern will not update when change an element. If not provided this default to True.   This is an optional argument whose default value is null. |
| Fitted | Variant | Optional input Boolean that specifies whether pattern elements are equally fitted within the specified distances. If set to False, the pattern spacing measures the distance between elements instead of the overall distance for the pattern. If not provided this default to False.   This is an optional argument whose default value is null. |
| SuppressedElements | Variant | Optional input Long array that specifies the indices of the elements to be suppressed.   This is an optional argument whose default value is null. |
| Reserved | Variant | Reserved for future use.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2025.1

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |