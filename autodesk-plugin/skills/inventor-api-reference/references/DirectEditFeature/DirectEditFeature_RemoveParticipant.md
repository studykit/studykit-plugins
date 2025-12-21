# DirectEditFeature.RemoveParticipant Method

Parent Object: [DirectEditFeature](../DirectEditFeature/DirectEditFeature.md)

## Description

Method that removes the specified participant from the assembly feature. This method fails for features in a part.

## Syntax

DirectEditFeature.**RemoveParticipant**( ***Occurrence*** As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Occurrence | [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) | ComponentOccurrence object that specifies the participant to be removed. An error occurs if the input ComponentOccurrence is not a participant. |

## Version

Introduced in version 2015
