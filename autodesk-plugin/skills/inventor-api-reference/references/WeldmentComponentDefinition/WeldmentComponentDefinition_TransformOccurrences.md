# WeldmentComponentDefinition.TransformOccurrences Method

Parent Object: [WeldmentComponentDefinition](../WeldmentComponentDefinition/WeldmentComponentDefinition.md)

## Description

Method that transforms a collection of occurrences.

## Syntax

WeldmentComponentDefinition.**TransformOccurrences**( ***Occurrences*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), ***Transforms*** As [ObjectCollection](../ObjectCollection/ObjectCollection.md), [***IgnoreConstraints***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Occurrences | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains the ComponentOccurrence objects to be transformed. The collection can only contain top level occurrences from the document. An exception is the case of a flexible occurrence within the top level assembly, in which case, deeper level occurrences may be provided. |
| Transforms | [ObjectCollection](../ObjectCollection/ObjectCollection.md) | Input ObjectCollection that contains Matrix objects defining the transform for the input occurrences. The collection must have the same number of objects as the number of input occurrences, else the method returns an error. The collection can also contain a single Matrix, in which case all occurrences are transformed similarly using the single Matrix. |
| IgnoreConstraints | Boolean | Optional input Boolean which specifies whether to transform the occurrences without re-applying the current assembly constraints. An update of the Assembly will honor the constraints and ignore these transforms. If not specified, a default value of False is used (i.e. constraints are honored). |

## Version

Introduced in version 2009
