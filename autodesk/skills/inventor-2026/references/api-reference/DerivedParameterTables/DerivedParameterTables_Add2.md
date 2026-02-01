# DerivedParameterTables.Add2 Method

Parent Object: [DerivedParameterTables](../DerivedParameterTables/DerivedParameterTables.md)

## Description

Method that creates a new DerivedParameterTable object, given an existing Inventor part or assembly document as input. Returns the resulting DerivedParameterTable object. This method fails if the input document has already been linked.

## Syntax

DerivedParameterTables.**Add2**( ***FullFileName*** As String, [***ParametersToLink***] As Variant ) As [DerivedParameterTable](../DerivedParameterTable/DerivedParameterTable.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| FullFileName | String | Input String value that contains the full path to the part or assembly document. |
| ParametersToLink | Variant | Optional input ObjectCollection that specifies the parameters in the input file to link. If this argument is not specified, all the exported parameters in the input file are linked. If there are no exported parameters, the method will fail. If specified, all parameters in the input file that are not already exported are automatically exported. |

## Version

Introduced in version 2008
