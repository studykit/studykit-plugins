# BendFeatures.CreateBendDefinition Method

Parent Object: [BendFeatures](../BendFeatures/BendFeatures.md)

## Description

Method that creates a new BendDefinition object. This object is not a bend feature but contains the information that defines bend information and can be used to help create a new feature that contains bends or edit the bend of an existing feature.

## Syntax

BendFeatures.**CreateBendDefinition**( ***Edges*** As [EdgeCollection](../EdgeCollection/EdgeCollection.md) ) As [BendDefinition](../BendDefinition/BendDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Edges | [EdgeCollection](../EdgeCollection/EdgeCollection.md) | Input EdgeCollection object that defines the existing edges on the sheet metal part that you want to create bends for. The EdgeCollection can contain either one or two edges depending on the geometry where you want to apply the bend and the type of feature the definition is being used with. To best understand what's valid you should try creating the same feature interactively to see what edges can be selected to create a valid bend. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create sheet metal rip feature](../../sample-programs/RipFeatures_Add_Sample.md) | This sample demonstrates the creation of a rip sheet metal feature. |

## Version

Introduced in version 2010
