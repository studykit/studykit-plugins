# PunchToolFeatures.Add Method

Parent Object: [PunchToolFeatures](../PunchToolFeatures/PunchToolFeatures.md)

## Description

Creates a new PunchToolFeature using the input placement information.

## Syntax

PunchToolFeatures.**Add**( ***PunchCenterPoints*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Definition*** As [iFeatureDefinition](../iFeatureDefinition/iFeatureDefinition.md), [***Angle***] As Variant, [***AcrossBends***] As Boolean ) As [PunchToolFeature](../PunchToolFeature/PunchToolFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| PunchCenterPoints | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection of SketchPoint objects that define the placement position(s) of the punch tool. All of the supplied SketchPoint objects must be owned by the same sketch. |
| Definition | [iFeatureDefinition](../iFeatureDefinition/iFeatureDefinition.md) | Input iFeatureDefinition object used to define the various input required for the placement of a PunchToolFeature. Appropriate input must be defined in the iFeatureDefinition object in order to place the punch tool. |
| Angle | Variant | Optional Input Variant that defines the placement angle of the punch tool. If not supplied, the punch tool will be placed with a rotation angle of zero. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are radians. If a string is input, the units can be specified as part of the string or it will default to the current angle units of the document. |
| AcrossBends | Boolean | Input Boolean specifies whether the punch tool feature goes across bends or not.   This is an optional argument whose default value is False. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Add a punch tool feature](../../sample-programs/PunchToolFeatures_Add_Sample.md) | This program demonstrates the creation of a punch tool feature. It uses one of the punch features that's delivered with Inventor. It assumes you already have an existing sheet metal part and have selected a face to place the punch feature on. The selected face should be large so there is room for the punch features. |

## Version

Introduced in version 2009
