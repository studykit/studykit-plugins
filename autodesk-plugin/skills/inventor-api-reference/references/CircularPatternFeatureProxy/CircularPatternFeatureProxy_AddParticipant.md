# CircularPatternFeatureProxy.AddParticipant Method

Parent Object: [CircularPatternFeatureProxy](../CircularPatternFeatureProxy/CircularPatternFeatureProxy.md)

## Description

Method that adds the specified participant to the assembly feature. This method fails for features in a part.

## Syntax

CircularPatternFeatureProxy.**AddParticipant**( ***Occurrence*** As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Occurrence | [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) | Input ComponentOccurrence object that specifies the participant to be added. An error occurs if the input ComponentOccurrence is not a leaf occurrence. |

## Version

Introduced in version 2010
