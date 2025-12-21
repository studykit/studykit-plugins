# InsertConstraint.ConvertToCustomConstraint Method

Parent Object: [InsertConstraint](../InsertConstraint/InsertConstraint.md)

## Description

Method that converts the constraint to a custom constraint, and returns the CustomConstraint object. This method can also be used to edit the geometries associated with a custom constraint without changing its type, in which case the same object is returned by the method.

## Syntax

InsertConstraint.**ConvertToCustomConstraint**( ***EntityOne*** As Object, ***EntityTwo*** As Object, ***ClientId*** As String ) As [CustomConstraint](CustomConstraint.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| EntityOne | Object | Input object that defines the first object. |
| EntityTwo | Object | Input object that defines the second object. |
| ClientId | String | Input String that specifies the ClientId, typically the ClassId of the Add-in creating the constraint. |

## Version

Introduced in version 2011
