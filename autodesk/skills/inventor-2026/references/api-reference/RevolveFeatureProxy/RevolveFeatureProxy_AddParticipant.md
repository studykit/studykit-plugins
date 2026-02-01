# RevolveFeatureProxy.AddParticipant Method

Parent Object: [RevolveFeatureProxy](../RevolveFeatureProxy/RevolveFeatureProxy.md)

## Description

Method that adds the specified participant to the assembly feature. This method fails for features in a part.

## Syntax

RevolveFeatureProxy.**AddParticipant**( ***Occurrence*** As [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Occurrence | [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md) | ComponentOccurrence object that specifies the participant to be added. An error occurs if the input ComponentOccurrence is not a leaf occurrence. |

## Version

Introduced in version 11
