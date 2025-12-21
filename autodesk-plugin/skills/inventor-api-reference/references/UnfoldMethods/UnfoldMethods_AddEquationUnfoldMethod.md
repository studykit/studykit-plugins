# UnfoldMethods.AddEquationUnfoldMethod Method

Parent Object: [UnfoldMethods](../UnfoldMethods/UnfoldMethods.md)

## Description

Method that adds an equation linear unfold method to the collection and returns the created UnfoldMethod object. The new unfold method will have a single equation that specifies that the bend compensation will be 0 for a bend from 0 to 180 degrees. You can edit the equation to the desired equation using the functionality of the returned UnfoldMethod object.

## Syntax

UnfoldMethods.**AddEquationUnfoldMethod**( ***Name*** As String ) As [UnfoldMethod](../UnfoldMethod/UnfoldMethod.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Name | String | Input String used to specify the name of the UnfoldMethod. This name must be unique with respect to other UnfoldMethod objects. If a unique name is not provided, an error will occur. |

## Version

Introduced in version 2011
