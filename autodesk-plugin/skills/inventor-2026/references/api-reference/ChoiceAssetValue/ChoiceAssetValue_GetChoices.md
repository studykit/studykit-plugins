# ChoiceAssetValue.GetChoices Method

Parent Object: [ChoiceAssetValue](../ChoiceAssetValue/ChoiceAssetValue.md)

## Description

Method that returns the valid choices associated with this value.

## Syntax

ChoiceAssetValue.**GetChoices**( ***Names***() As String, ***Choices***() As String )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Names | String | Output array or strings that contains the valid id’s that can be used when setting the value of this asset. |
| Choices | String | Output array of strings that contains the localized names for the choices. These are returned in a corresponding order to the id’s returned in the Names argument. |

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Write out all appearance information to a file.](../../sample-programs/DumpAllAppearances_Sample.md) | This sample writes out information about all of the appearances in all libraries. This can be useful when trying to use the API to modify existing appearances by allowing to easily see what information is available for an appearance. |
| [Write out all materials to a file.](../../sample-programs/DumpAllMaterials_Sample.md) | This sample writes out information about all of the materials in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a material. |
| [Write out all physical properties to a file.](../../sample-programs/DumpAllPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in all libraries. This can be useful when trying to use the API to modify existing materials by allowing to easily see what information is available for a physical property. |
| [Write out all document appearances](../../sample-programs/DumpDocumentAppearances_Sample.md) | This sample writes out information about all of the appearances in the active document. This can be useful when trying to use the API to modify existing appearances by allowing you to easily see what information is available for an appearance. |
| [Write out all document materials to a file.](../../sample-programs/DumpDocumentMaterials_Sample.md) | This sample writes out information about all of the materials in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a material. |
| [Write out all document physical properties to a file.](../../sample-programs/DumpDocumentPhysicalProperties_Sample.md) | This sample writes out information about all of the physical properties in the active document. This can be useful when trying to use the API to modify existing materials by allowing you to easily see what information is available for a physical property |

## Version

Introduced in version 2014
