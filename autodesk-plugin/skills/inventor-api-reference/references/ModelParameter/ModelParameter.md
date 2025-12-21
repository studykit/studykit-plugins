# ModelParameter Object

Derived from: [Parameter](../Parameter/Parameter.md) Object

## Description

Object that represents a parameter that was created automatically by Autodesk Inventor as the result of creating an object that is dependent on a parameter. For example, when a placing a driving dimension constraint a ModelParameter is automatically created to control the dimension.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToReferenceParameter](../ModelParameter/ModelParameter_ConvertToReferenceParameter.md) | Method that causes the parameter to be converted to a reference parameter. The new ReferenceParameter object is returned. This method will fail if this is a built-in parameter (indicated by the BuiltIn property). |
| [ConvertToUserParameter](../ModelParameter/ModelParameter_ConvertToUserParameter.md) | Method that causes the parameter to be converted to a user parameter. The new UserParameter object is returned. This method will fail if this is a built-in parameter (indicated by the BuiltIn property). |
| [Delete](../ModelParameter/ModelParameter_Delete.md) | Method that deletes this Parameter. |
| [GetReferenceKey](../ModelParameter/ModelParameter_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AttributeSets](../ModelParameter/ModelParameter_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BuiltIn](../ModelParameter/ModelParameter_BuiltIn.md) | Property that returns whether this is an Inventor-generated parameter or an API-created one. Returns True if it is Inventor-generated. |
| [Comment](../ModelParameter/ModelParameter_Comment.md) | Gets the user comments against this parameter. |
| [CustomPropertyFormat](../ModelParameter/ModelParameter_CustomPropertyFormat.md) | Property that returns the CustomPropertyFormat object associated with this parameter. The CustomPropertyFormat provides control over how the parameter value is formatted when it is exposed as a custom iProperty. |
| [Dependents](../ModelParameter/ModelParameter_Dependents.md) | Property that returns the collection of objects that have a direct dependency on the parameter. |
| [DisabledActionTypes](../ModelParameter/ModelParameter_DisabledActionTypes.md) | Gets and sets the action types valid for this parameter. |
| [DisplayFormat](../ModelParameter/ModelParameter_DisplayFormat.md) | Gets and sets the display format for the parameter. |
| [DrivenBy](../ModelParameter/ModelParameter_DrivenBy.md) | Method that returns the collection objects that the parameter is dependent on. |
| [ExposedAsProperty](../ModelParameter/ModelParameter_ExposedAsProperty.md) | Gets/(Sets) the Boolean indicating if this parameter is exposed as a property of this Document. |
| [Expression](../ModelParameter/ModelParameter_Expression.md) | Gets/(Sets) the string that denotes the algebraic expression making up the definition of this parameter. Maybe a constant. 'Set' may not be allowed on some parameter types. When set this for Text parameter, the expression value should be quoted by quotation marks at beginning and ending of a string(like """I am Jack"""). |
| [ExpressionList](../ModelParameter/ModelParameter_ExpressionList.md) | Property that returns the expression list associated with this parameter. |
| [HealthStatus](../ModelParameter/ModelParameter_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InUse](../ModelParameter/ModelParameter_InUse.md) | Property that returns whether whether this parameter is currently in use (by a dimension, feature or by any other parameter). |
| [IsKey](../ModelParameter/ModelParameter_IsKey.md) | Gets and sets whether this parameter is a key parameter or not. Key parameters are typically those that need to be easily accessed and are designated as key to be filtered out from the rest of the parameters. |
| [ModelValue](../ModelParameter/ModelParameter_ModelValue.md) | Property that returns the evaluation of this parameter (in database units) that is currently used by the model. This takes into account the value computed from the expression and the tolerance. This method is only valid for numeric unit types and will fail for Text and Boolean unit types. |
| [ModelValueType](../ModelParameter/ModelParameter_ModelValueType.md) | Gets/(Sets) the setting which is used for determining the method used to compute the model value. |
| [Name](../ModelParameter/ModelParameter_Name.md) | Gets/Sets the name of this parameter. |
| [ParameterType](../ModelParameter/ModelParameter_ParameterType.md) | Property that allows you to get the type of the parameter. The parameter type can be either kModelParameterType, kDerivedParameter, kFinishParameter, kReferenceParameterType, kTableParameterType, or kUserParameterType. |
| [Parent](../ModelParameter/ModelParameter_Parent.md) | Property that returns the parent Document of this parameter. |
| [Precision](../ModelParameter/ModelParameter_Precision.md) | Gets/(Sets) the the number of decimal places displayed for this parameter. Note that the precision is used when applying a standard tolerance to the parameter. |
| [Renamed](../ModelParameter/ModelParameter_Renamed.md) | Gets whether the ModelParameter has been renamed by the user. |
| [Tolerance](../ModelParameter/ModelParameter_Tolerance.md) | Property that returns the tolerance for this parameter. This property returns Nothing in the case where the unit type of this parameter is kTextUnits or kBooleanUnits. |
| [Type](../ModelParameter/ModelParameter_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Units](../ModelParameter/ModelParameter_Units.md) | Gets/(Sets) the units of the parameter. Note that the units is always retrieved as a string, but may be set using a constant from UnitsTypeEnum. 'Set' may not be allowed on some parameter types. |
| [Value](../ModelParameter/ModelParameter_Value.md) | Gets/(Sets) the value of this parameter. Numeric values are in database units. Setting this is equivalent to setting the 'Expression' with a constant string. 'Set' may not be allowed on some parameter types. |

## Accessed From

[ModelParameters.AddByExpression](../ModelParameters/ModelParameters_AddByExpression.md), [ModelParameters.AddByValue](../ModelParameters/ModelParameters_AddByValue.md), [ModelParameters.Item](../ModelParameters/ModelParameters_Item.md), [ReferenceParameter.ConvertToModelParameter](../ReferenceParameter/ReferenceParameter_ConvertToModelParameter.md), [UserParameter.ConvertToModelParameter](../UserParameter/UserParameter_ConvertToModelParameter.md)

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