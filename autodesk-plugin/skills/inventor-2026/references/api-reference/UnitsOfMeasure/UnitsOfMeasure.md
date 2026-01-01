# UnitsOfMeasure Object

## Description

The UnitsOfMeasure object supports various functions to allow you to interact with the units associated with the document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CompatibleUnits](../UnitsOfMeasure/UnitsOfMeasure_CompatibleUnits.md) | Method that evaluates the two input expressions and determines if the result in units that have the same base unit type. |
| [ConvertUnits](../UnitsOfMeasure/UnitsOfMeasure_ConvertUnits.md) | Method that converts a value from one unit to another. The input and output unit specifiers must both define compatible units. For example, "in" (inches) and "cm" (centimeters) will work because they both define lengths. If incompatible units are specified, this method will fail. The converted value, in the units specified by the OutputUnitsSpecifier argument is returned. |
| [GetDatabaseUnitsFromExpression](../UnitsOfMeasure/UnitsOfMeasure_GetDatabaseUnitsFromExpression.md) | Evaluates an input string and returns equivalent database units as a string. |
| [GetDrivingParameters](../UnitsOfMeasure/UnitsOfMeasure_GetDrivingParameters.md) | Obtains the driving parameters enumerator corresponding to the input string. |
| [GetLocaleCorrectedExpression](../UnitsOfMeasure/UnitsOfMeasure_GetLocaleCorrectedExpression.md) | This method converts the input expression to a locale-friendly version. For instance, if you input "1.0 in" on a machine set to the German locale, the return value is "1,0 in". In this case, the decimal separator is different. |
| [GetPreciseStringFromValue](../UnitsOfMeasure/UnitsOfMeasure_GetPreciseStringFromValue.md) | Obtains the precise string along with the units, given a value. The output units needs to be specified as well. |
| [GetStringFromType](../UnitsOfMeasure/UnitsOfMeasure_GetStringFromType.md) | Given a unit type from the UnitsTypeEnum as input, this method returns the string that can be used to specify the same unit type. |
| [GetStringFromValue](../UnitsOfMeasure/UnitsOfMeasure_GetStringFromValue.md) | Method that creates a string that represents the input value evaluated using the specified units. |
| [GetTypeFromString](../UnitsOfMeasure/UnitsOfMeasure_GetTypeFromString.md) | Given a string defining a unit this method returns the corresponding unit from the UnitsTypeEnum constant list. If the unit specified by the string does not exist in the constant list an error will occur. For example, inputting "mm" will return kMillimeterLengthUnits. This method is not currently supported when the UnitsOfMeasure object was obtained using Apprentice. |
| [GetValueFromExpression](../UnitsOfMeasure/UnitsOfMeasure_GetValueFromExpression.md) | Method that evaluates the input expression using the units specified and returns a value in database units. |
| [IsExpressionValid](../UnitsOfMeasure/UnitsOfMeasure_IsExpressionValid.md) | Returns whether the input expression is valid or not. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AngleDisplayPrecision](../UnitsOfMeasure/UnitsOfMeasure_AngleDisplayPrecision.md) | Gets/Sets the number of places to display after the decimal point, when displaying an angle value. |
| [AngleUnits](../UnitsOfMeasure/UnitsOfMeasure_AngleUnits.md) | Gets/Sets the default unit of angle for this Document. |
| [LengthDisplayPrecision](../UnitsOfMeasure/UnitsOfMeasure_LengthDisplayPrecision.md) | Gets/Sets the number of places to display after the decimal point, when displaying a length value. |
| [LengthUnits](../UnitsOfMeasure/UnitsOfMeasure_LengthUnits.md) | Gets/Sets the default unit of length for this Document. |
| [MassUnits](../UnitsOfMeasure/UnitsOfMeasure_MassUnits.md) | Gets/Sets the default unit of mass for this Document. |
| [Parent](../UnitsOfMeasure/UnitsOfMeasure_Parent.md) | Property returning the parent Document object. |
| [TimeUnits](../UnitsOfMeasure/UnitsOfMeasure_TimeUnits.md) | Gets/Sets the default unit of time for this Document. |
| [Type](../UnitsOfMeasure/UnitsOfMeasure_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[Application.UnitsOfMeasure](../Application/Application_UnitsOfMeasure.md), [ApprenticeServerDocument.UnitsOfMeasure](../ApprenticeServerDocument/ApprenticeServerDocument_UnitsOfMeasure.md), [ApprenticeServerDrawingDocument.UnitsOfMeasure](../ApprenticeServerDrawingDocument/ApprenticeServerDrawingDocument_UnitsOfMeasure.md), [AssemblyDocument.UnitsOfMeasure](../AssemblyDocument/AssemblyDocument_UnitsOfMeasure.md), [Document.UnitsOfMeasure](../Document/Document_UnitsOfMeasure.md), [DrawingDocument.UnitsOfMeasure](../DrawingDocument/DrawingDocument_UnitsOfMeasure.md), [InventorServer.UnitsOfMeasure](InventorServer_UnitsOfMeasure.md), [InventorServerObject.UnitsOfMeasure](InventorServerObject_UnitsOfMeasure.md), [PartDocument.UnitsOfMeasure](../PartDocument/PartDocument_UnitsOfMeasure.md), [PresentationDocument.UnitsOfMeasure](../PresentationDocument/PresentationDocument_UnitsOfMeasure.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Client graphics texture-based color mapping](../../sample-programs/GraphicsColorMapper_Sample.md) | This test applies texture coordinates expressing distance from the origin to 'the triangle mesh of whatever Part you have open. It then creates either a discrete-band or continuous color mapper and allows you to adjust the values of the mapper to change the range of values that map to various colors. |
| [Create or update custom iProperty](../../sample-programs/iPropertyCreateUpdateCustom_Sample.md) | This example creates a custom iProperty if it doesn't exist and updates the value if it does already exist. A part document must be open before runnin the sample. |
| [Using measure events](../../sample-programs/MeasureEventsSink_OnMeasure_Sample.md) | This sample demonstrates using the measure events to measure distance and angle. Interactive measure is dependent on events and VB only supports events within a class module. To use the sample copy the InteractiveMeasureDistance and InteractiveMeasureAngle subs into a code module. Create a new class module called clsMeasure and copy all of the rest of the code into it. |

## Version

Introduced in version 4
