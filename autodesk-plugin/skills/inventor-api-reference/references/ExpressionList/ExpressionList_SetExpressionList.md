# ExpressionList.SetExpressionList Method

Parent Object: [ExpressionList](../ExpressionList/ExpressionList.md)

## Description

Method that sets the list of expressions for the parameter this expression list is associated with. The current value of the associated parameter will be modifed to match one of the values in the list. The CurrentValueIndex argument allows you control over which value from the list is used.

## Syntax

ExpressionList.**SetExpressionList**( ***ExpressionList***() As String, [***ChangeCurrentValue***] As Boolean, [***CurrentValueIndex***] As Long )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| ExpressionList | String | Input array of Strings that defines a list of valid expressions that the user will be able to select from when setting the value of the associated parameter. When set this for Text parameter, the expression value should be quoted by quotation marks at beginning and ending of a string(like """I am Jack"""). |
| ChangeCurrentValue | Boolean | Optional input Boolean value indicating whether to change the current value or not. When set this to True then you can use CurrentValueIndex to specify which value in the expression list to use as current value.   This is an optional argument whose default value is False. |
| CurrentValueIndex | Long | Input Long value that specifies which value within the expression list should be used as the current value of the parameter. The first value in the expression list is index 0.  For a numerical parameter, the default value of -1 will result in the expression that is closest to the current value of the parameter being used." Otherwise the index value specified will be used.  For a String parameter, the default value of -1 will result in using the value from the list if there's one that matches the current value of the parameter. If -1 is specified and the current parameter value doesn't match one of the values in the list the first value in the list is used.  This method is not valid for Boolean type parameters since they are already limited to True or False.   This is an optional argument whose default value is -1. |

## Version

Introduced in version 2011
