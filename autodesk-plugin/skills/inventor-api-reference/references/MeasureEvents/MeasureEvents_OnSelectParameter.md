# MeasureEvents.OnSelectParameter Event

Parent Object: [MeasureEvents](../MeasureEvents/MeasureEvents.md)

## Description

Event that fires when the user selects a parameter. The selected object can be a feature dimension, a 2d sketch dimension, a 3d sketch dimension or a parameter from the parameters list box.

## Syntax

MeasureEvents.**OnSelectParameter**( ***Parameter*** As [Parameter](../Parameter/Parameter.md), ***Context*** As [NameValueMap](../NameValueMap/NameValueMap.md) )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Parameter | [Parameter](../Parameter/Parameter.md) | Input Parameter object selected by the user. This parameter can either be associated with a dimension or could be a parameter created by the user or via the API. |
| Context | [NameValueMap](../NameValueMap/NameValueMap.md) | Currently empty. |

## Version

Introduced in version 2009
