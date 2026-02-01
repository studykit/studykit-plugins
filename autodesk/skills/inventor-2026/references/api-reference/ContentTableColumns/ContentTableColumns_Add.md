# ContentTableColumns.Add Method

Parent Object: [ContentTableColumns](../ContentTableColumns/ContentTableColumns.md)

## Description

Method that creates a new column. Any changes to the table are not actually applied until the Save method of the parent ContentFamily object is called.

## Syntax

ContentTableColumns.**Add**( ***InternalName*** As String, ***DisplayHeading*** As String, ***DataType*** As [ValueTypeEnum](../ValueTypeEnum.md), [***Units***] As Variant, [***Expression***] As Variant, [***PropertySetId***] As Variant, [***PropertyIdentifier***] As Variant ) As [ContentTableColumn](../ContentTableColumn/ContentTableColumn.md)

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| InternalName | String | Input String that specifies the internal name of this column. |
| DisplayHeading | String | Input String that specifies the display name of this column. This is the name of the column that the end-user sees within the user interface. |
| DataType | [ValueTypeEnum](../ValueTypeEnum.md) | Input value from ValueTypeEnum that specifies the type of data within this column. Valid values are: kIntegerType, kDoubleType, kStringType, and kBooleanType. |
| Units | Variant | Input value that specifies the type of unit the values in the column are. The unit type needs to be specified if the DataType argument is kIntegerType or kDoubleType. For kStringType and kBooleanType this argument is ignored.  You specify a unit type using a value from UnitsTypeEnum or a string that describes a unit. For example, both of the following are valid unit specifiers for inch: kInchLengthUnits and "in". String specifiers are typically used for units that are not defined in the enum list. For example, the volume measure for cubic inches is not defined in the enum list but you can specify it using the string "in in in". |
| Expression | Variant | Optional input Variant that specifies the expression to use to automatically populate the rows of this column. Not supplying this argument or providing an empty String will result in the default value of '1' being used.  There are two things that can be defined for the expression, a standard expression and limits for a custom expression. These are defined below.  **Standard Expression** ' This allows you to define an expression and will evaluate it to populate the rows of the table. Expressions can contain expression like you would use to define the value of a parameter and they can also contain the values of other columns. To use the values of other columns enclose the internal name within braces. Here are some examples of valid expression strings.  `20 in`  `{SIZE}`  `{TOTAL_LENGTH} ' {HEAD_HEIGHT}`  `{DIA} / 2`  **Custom Expression Limits**' A custom expression allows the end-user to specify the value when placing the member into an assembly. You can choose to define the limits for this value, i.e. minimum, maximum, increment and default values. These rules are defined using an ExpressionLimits object. You can create this object using the ContentTableColumn.CreateExpressionLimits method.    This is an optional argument whose default value is null. |
| PropertySetId | Variant | Optional input String that specifies the name of the property set that contains the property. This is the InternalName or Name associated with the property set. If this argument is set you must also set the PropertyIdentifier argument to fully define the property to use.   This is an optional argument whose default value is null. |
| PropertyIdentifier | Variant | Optional input Variant that identifies a property. This can be a Long value that specifies the PropId or the name of a property. If this argument is set you must also set the PropertySetId argument to fully define the property to use.   This is an optional argument whose default value is null. |

## Version

Introduced in version 2010
