# ExpressionList Object

## Description

The ExpressionList provides access to a list of possible expressions that can be used for the associated parameter.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ClearAll](../ExpressionList/ExpressionList_ClearAll.md) | Method that removes all items from the list. |
| [GetExpressionList](../ExpressionList/ExpressionList_GetExpressionList.md) | Rreturns an array of Strings that represents the list of expressions used in the list. |
| [SetExpressionList](../ExpressionList/ExpressionList_SetExpressionList.md) | Method that sets the list of expressions for the parameter this expression list is associated with. The current value of the associated parameter will be modifed to match one of the values in the list. The CurrentValueIndex argument allows you control over which value from the list is used. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AllowCustomValues](../ExpressionList/ExpressionList_AllowCustomValues.md) | Gets/Sets whether to allow users to specify custom values. |
| [Application](../ExpressionList/ExpressionList_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [Count](../ExpressionList/ExpressionList_Count.md) | Property that specifies the number of expressions in the list. |
| [CustomOrder](../ExpressionList/ExpressionList_CustomOrder.md) | Read-write property that gets and sets whether to disable automatically sorting the custom values. If you assign a list of values using SetExpressionList, that operation will automatically set CustomOrder to True. If you want to assign a list using SetExpressi. |
| [Item](../ExpressionList/ExpressionList_Item.md) | Property that gets the specified expression in the list. |
| [Parent](../ExpressionList/ExpressionList_Parent.md) | Property that returns the parent Parameter object. |
| [Type](../ExpressionList/ExpressionList_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[DerivedParameter.ExpressionList](../DerivedParameter/DerivedParameter_ExpressionList.md), [FinishParameter.ExpressionList](../FinishParameter/FinishParameter_ExpressionList.md), [ModelParameter.ExpressionList](../ModelParameter/ModelParameter_ExpressionList.md), [Parameter.ExpressionList](../Parameter/Parameter_ExpressionList.md), [ReferenceParameter.ExpressionList](../ReferenceParameter/ReferenceParameter_ExpressionList.md), [TableParameter.ExpressionList](../TableParameter/TableParameter_ExpressionList.md), [UserParameter.ExpressionList](../UserParameter/UserParameter_ExpressionList.md)

## Version

Introduced in version 2011

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |