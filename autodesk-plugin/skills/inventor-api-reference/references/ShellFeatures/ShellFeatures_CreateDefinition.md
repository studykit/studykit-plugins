# ShellFeatures.CreateDefinition Method

Parent Object: [ShellFeatures](../ShellFeatures/ShellFeatures.md)

## Description

Method that creates a new ShellDefinition object. The object returned by this method isused to define the inputs for a shell feature and is provided as the argument to the Add method of the ShellFeatures collection.

## Syntax

ShellFeatures.**CreateDefinition**( [***InputFaces***] As Variant, [***Solids***] As Variant, [***Thickness***] As Variant, [***Direction***] As [ShellDirectionEnum](../ShellDirectionEnum.md), [***Method***] As [ShellMethodEnum](../ShellMethodEnum.md), [***MoreOptions***] As Variant ) As [ShellDefinition](../ShellDefinition/ShellDefinition.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InputFaces | Variant | Optional input FaceCollection object that defines the part faces to remove, leaving the remaining faces as shell walls. If the argument is not specified, the Solids argument can be used to specify the SurfaceBody objects to hollow out. |
| Solids | Variant | Optional input ObjectCollection that specifies the SurfaceBody objects being hollowed out. If the InputFaces and this Solids are both not specified then the first solid SurfaceBody will be used to hollow out if applicable, otherwise an error would occur when create a shell feature. If the InputFaces argument is specified and this argument is not specified the SurfaceBody objects containing the input faces will be automatically included in the Solids after this definition is created. If the InputFaces argument is specified and this argument is specified also the SurfaceBody objects containing the input faces should be provided in this Solids argument also.   This is an optional argument whose default value is null. |
| Thickness | Variant | Optional input Variant that specifies the thickness to be applied uniformly to shell walls. This can be either a numeric value or a string. A parameter for this value will be created and the supplied string or value is assigned to the parameter. If a value is input, the units are centimeters. If a string is input, the units can be specified as part of the string or it will default to the current distance units of the document.   This is an optional argument whose default value is null. |
| Direction | [ShellDirectionEnum](../ShellDirectionEnum.md) | Optional input ShellDirectionEnum that specifies the shell boundary relative to the part face. Valid inputs are kInsideShellDirection that offsets the shell wall to the part interior, kOutsideShellDirection that offsets the shell wall to the exterior of the part, and kBothSidesShellDirection that offsets the shell wall equal distances to inside and outside the part. The default value is kInsideShellDirection.   This is an optional argument whose default value is 41217. |
| Method | [ShellMethodEnum](../ShellMethodEnum.md) | Optional input ShellMethodEnum that specifies the shell method type. Valid inputs are kSharpShellMethod and kRoundedShellMethod. The default value is kSharpShellMethod.   This is an optional argument whose default value is 130305. |
| MoreOptions | Variant | Optional input NameValueMap that specifies more options. This is reserved for future use.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2026
