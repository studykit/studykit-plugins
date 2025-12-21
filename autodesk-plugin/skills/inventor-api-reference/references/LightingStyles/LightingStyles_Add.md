# LightingStyles.Add Method

Parent Object: [LightingStyles](../LightingStyles/LightingStyles.md)

## Description

Method that creates a new LightingStyle object. The name of the new style is specified, while the rendering attributes are initialized with the same values as the Default style.

## Syntax

LightingStyles.**Add**( ***Name*** As String ) As [LightingStyle](../LightingStyle/LightingStyle.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String that specifies the name of the new rendering style. This name must be unique with respect to all other rendering styles defined in the document. The method will fail if the name is not unique. |

## Version

Introduced in version 10
