# UserParameter Object

Derived from: [Parameter](../Parameter/Parameter.md) Object

## Description

Object that represents a parameter that was created by the user.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToModelParameter](../UserParameter/UserParameter_ConvertToModelParameter.md) | Method that causes the parameter to be converted to a model parameter. The new ModelParameter object is returned. |
| [ConvertToReferenceParameter](../UserParameter/UserParameter_ConvertToReferenceParameter.md) | Method that causes the parameter to be converted to a reference parameter. The new ReferenceParameter object is returned. |
| [Delete](../UserParameter/UserParameter_Delete.md) | Method that deletes this Parameter. |
| [GetReferenceKey](../UserParameter/UserParameter_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AttributeSets](../UserParameter/UserParameter_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Comment](../UserParameter/UserParameter_Comment.md) | Gets the user comments against this parameter. |
| [CustomPropertyFormat](../UserParameter/UserParameter_CustomPropertyFormat.md) | Property that returns the CustomPropertyFormat object associated with this parameter. The CustomPropertyFormat provides control over how the parameter value is formatted when it is exposed as a custom iProperty. |
| [Dependents](../UserParameter/UserParameter_Dependents.md) | Property that returns the collection of objects that have a direct dependency on the parameter. |
| [DisabledActionTypes](../UserParameter/UserParameter_DisabledActionTypes.md) | Gets and sets the action types valid for this parameter. |
| [DisplayFormat](../UserParameter/UserParameter_DisplayFormat.md) | Gets and sets the display format for the parameter. |
| [DrivenBy](../UserParameter/UserParameter_DrivenBy.md) | Method that returns the collection objects that the parameter is dependent on. |
| [ExposedAsProperty](../UserParameter/UserParameter_ExposedAsProperty.md) | Gets/(Sets) the Boolean indicating if this parameter is exposed as a property of this Document. |
| [Expression](../UserParameter/UserParameter_Expression.md) | Gets/(Sets) the string that denotes the algebraic expression making up the definition of this parameter. Maybe a constant. 'Set' may not be allowed on some parameter types. When set this for Text parameter, the expression value should be quoted by quotation marks at beginning and ending of a string(like """I am Jack"""). |
| [ExpressionList](../UserParameter/UserParameter_ExpressionList.md) | Property that returns the expression list associated with this parameter. |
| [HealthStatus](../UserParameter/UserParameter_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InUse](../UserParameter/UserParameter_InUse.md) | Property that returns whether whether this parameter is currently in use (by a dimension, feature or by any other parameter). |
| [IsKey](../UserParameter/UserParameter_IsKey.md) | Gets and sets whether this parameter is a key parameter or not. Key parameters are typically those that need to be easily accessed and are designated as key to be filtered out from the rest of the parameters. |
| [ModelValue](../UserParameter/UserParameter_ModelValue.md) | Property that returns the evaluation of this parameter (in database units) that is currently used by the model. This takes into account the value computed from the expression and the tolerance. This method is only valid for numeric unit types and will fail for Text and Boolean unit types. |
| [ModelValueType](../UserParameter/UserParameter_ModelValueType.md) | Gets/(Sets) the setting which is used for determining the method used to compute the model value. |
| [Name](../UserParameter/UserParameter_Name.md) | Gets/Sets the name of this parameter. |
| [ParameterType](../UserParameter/UserParameter_ParameterType.md) | Property that allows you to get the type of the parameter. The parameter type can be either kModelParameterType, kDerivedParameter, kFinishParameter, kReferenceParameterType, kTableParameterType, or kUserParameterType. |
| [Parent](../UserParameter/UserParameter_Parent.md) | Property that returns the parent Document of this parameter. |
| [Precision](../UserParameter/UserParameter_Precision.md) | Gets/(Sets) the the number of decimal places displayed for this parameter. Note that the precision is used when applying a standard tolerance to the parameter. |
| [Tolerance](../UserParameter/UserParameter_Tolerance.md) | Property that returns the tolerance for this parameter. This property returns Nothing in the case where the unit type of this parameter is kTextUnits or kBooleanUnits. |
| [Type](../UserParameter/UserParameter_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Units](../UserParameter/UserParameter_Units.md) | Gets/(Sets) the units of the parameter. Note that the units is always retrieved as a string, but may be set using a constant from UnitsTypeEnum. 'Set' may not be allowed on some parameter types. |
| [Value](../UserParameter/UserParameter_Value.md) | Gets/(Sets) the value of this parameter. Numeric values are in database units. Setting this is equivalent to setting the 'Expression' with a constant string. 'Set' may not be allowed on some parameter types. |

## Accessed From

[ModelParameter.ConvertToUserParameter](../ModelParameter/ModelParameter_ConvertToUserParameter.md), [ReferenceParameter.ConvertToUserParameter](../ReferenceParameter/ReferenceParameter_ConvertToUserParameter.md), [TableParameter.ConvertToUserParameter](../TableParameter/TableParameter_ConvertToUserParameter.md), [UserParameters.AddByExpression](../UserParameters/UserParameters_AddByExpression.md), [UserParameters.AddByValue](../UserParameters/UserParameters_AddByValue.md), [UserParameters.Item](../UserParameters/UserParameters_Item.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Creating a new parameter group](../../sample-programs/CustomParameterGroup_Add_Sample.md) | This sample demonstrates the creation of model, reference and user parameters and copying these parameters to a newly created group. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |