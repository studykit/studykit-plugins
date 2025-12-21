# TableParameter Object

Derived from: [Parameter](../Parameter/Parameter.md) Object

## Description

Object that represents a parameter that was created automatically by Autodesk Inventor as the result of reading a spreadsheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [ConvertToUserParameter](../TableParameter/TableParameter_ConvertToUserParameter.md) | Method that causes the parameter to be converted to a user parameter. The new UserParameter object is returned. |
| [Delete](../TableParameter/TableParameter_Delete.md) | Method that deletes this Parameter. |
| [GetReferenceKey](../TableParameter/TableParameter_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AttributeSets](../TableParameter/TableParameter_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [Comment](../TableParameter/TableParameter_Comment.md) | Gets the user comments against this parameter. |
| [CustomPropertyFormat](../TableParameter/TableParameter_CustomPropertyFormat.md) | Property that returns the CustomPropertyFormat object associated with this parameter. The CustomPropertyFormat provides control over how the parameter value is formatted when it is exposed as a custom iProperty. |
| [Dependents](../TableParameter/TableParameter_Dependents.md) | Property that returns the collection of objects that have a direct dependency on the parameter. |
| [DisabledActionTypes](../TableParameter/TableParameter_DisabledActionTypes.md) | Gets and sets the action types valid for this parameter. |
| [DisplayFormat](../TableParameter/TableParameter_DisplayFormat.md) | Gets and sets the display format for the parameter. |
| [DrivenBy](../TableParameter/TableParameter_DrivenBy.md) | Method that returns the collection objects that the parameter is dependent on. |
| [ExposedAsProperty](../TableParameter/TableParameter_ExposedAsProperty.md) | Gets/(Sets) the Boolean indicating if this parameter is exposed as a property of this Document. |
| [Expression](../TableParameter/TableParameter_Expression.md) | Gets/(Sets) the string that denotes the algebraic expression making up the definition of this parameter. Maybe a constant. 'Set' may not be allowed on some parameter types. When set this for Text parameter, the expression value should be quoted by quotation marks at beginning and ending of a string(like """I am Jack"""). |
| [ExpressionList](../TableParameter/TableParameter_ExpressionList.md) | Property that returns the expression list associated with this parameter. |
| [HealthStatus](../TableParameter/TableParameter_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [InUse](../TableParameter/TableParameter_InUse.md) | Property that returns whether whether this parameter is currently in use (by a dimension, feature or by any other parameter). |
| [IsKey](../TableParameter/TableParameter_IsKey.md) | Gets and sets whether this parameter is a key parameter or not. Key parameters are typically those that need to be easily accessed and are designated as key to be filtered out from the rest of the parameters. |
| [ModelValue](../TableParameter/TableParameter_ModelValue.md) | Property that returns the evaluation of this parameter (in database units) that is currently used by the model. This takes into account the value computed from the expression and the tolerance. This method is only valid for numeric unit types and will fail for Text and Boolean unit types. |
| [ModelValueType](../TableParameter/TableParameter_ModelValueType.md) | Gets/(Sets) the setting which is used for determining the method used to compute the model value. |
| [Name](../TableParameter/TableParameter_Name.md) | Gets/Sets the name of this parameter. |
| [ParameterType](../TableParameter/TableParameter_ParameterType.md) | Property that allows you to get the type of the parameter. The parameter type can be either kModelParameterType, kDerivedParameter, kFinishParameter, kReferenceParameterType, kTableParameterType, or kUserParameterType. |
| [Parent](../TableParameter/TableParameter_Parent.md) | Property that returns the parent Document of this parameter. |
| [Precision](../TableParameter/TableParameter_Precision.md) | Gets/(Sets) the the number of decimal places displayed for this parameter. Note that the precision is used when applying a standard tolerance to the parameter. |
| [Tolerance](../TableParameter/TableParameter_Tolerance.md) | Property that returns the tolerance for this parameter. This property returns Nothing in the case where the unit type of this parameter is kTextUnits or kBooleanUnits. |
| [Type](../TableParameter/TableParameter_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Units](../TableParameter/TableParameter_Units.md) | Gets/(Sets) the units of the parameter. Note that the units is always retrieved as a string, but may be set using a constant from UnitsTypeEnum. 'Set' may not be allowed on some parameter types. |
| [Value](../TableParameter/TableParameter_Value.md) | Gets/(Sets) the value of this parameter. Numeric values are in database units. Setting this is equivalent to setting the 'Expression' with a constant string. 'Set' may not be allowed on some parameter types. |

## Accessed From

[TableParameters.Item](../TableParameters/TableParameters_Item.md)

## Version

Introduced in version 4
