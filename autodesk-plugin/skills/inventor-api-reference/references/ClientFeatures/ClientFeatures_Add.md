# ClientFeatures.Add Method

Parent Object: [ClientFeatures](../ClientFeatures/ClientFeatures.md)

## Description

Method that creates a new ClientFeature. The newly created ClientFeature is returned.

## Syntax

ClientFeatures.**Add**( ***Definition*** As [ClientFeatureDefinition](../ClientFeatureDefinition/ClientFeatureDefinition.md), ***ClientId*** As String ) As [ClientFeature](../ClientFeature/ClientFeature.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Definition | [ClientFeatureDefinition](../ClientFeatureDefinition/ClientFeatureDefinition.md) | Input ClientFeatureDefinition object created using the CreateDefinition method. |
| ClientId | String | Input string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |

## Version

Introduced in version 2008
