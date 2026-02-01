# DecalFeatureProxy.RemoveParticipant Method

Parent Object: [DecalFeatureProxy](../DecalFeatureProxy/DecalFeatureProxy.md)

## Description

Method that removes the specified participant from the assembly feature. This method fails for features in a part.

## Syntax

DecalFeatureProxy.**RemoveParticipant**( ***Occurrence*** As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Occurrence | [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) | ComponentOccurrence object that specifies the participant to be removed. An error occurs if the input ComponentOccurrence is not a participant. |

## Version

Introduced in version 10
