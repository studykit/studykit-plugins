# AngularGeneralDimension Object

Derived from: [GeneralDimension](../GeneralDimension/GeneralDimension.md) Object

## Description

The AngularGeneralDimension object represents an angular general dimension placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [CenterText](../AngularGeneralDimension/AngularGeneralDimension_CenterText.md) | Method that centers the dimension text on the dimension line. |
| [Delete](../AngularGeneralDimension/AngularGeneralDimension_Delete.md) | Method that deletes the DrawingDimension. |
| [GetInspectionDimensionData](../AngularGeneralDimension/AngularGeneralDimension_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [GetReferenceKey](../AngularGeneralDimension/AngularGeneralDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [PromoteToSketch](../AngularGeneralDimension/AngularGeneralDimension_PromoteToSketch.md) | Method that copies the dimension to the underlying sketch. This method only works for dimensions associated with a draft view. |
| [SetInspectionDimensionData](../AngularGeneralDimension/AngularGeneralDimension_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn't already. |
| [ShowAllExtensionLines](../AngularGeneralDimension/AngularGeneralDimension_ShowAllExtensionLines.md) | Method that un-hides all the extension lines associated with this dimension. If there are no hidden extension lines associated with this dimension, this method does nothing and returns a success. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AngularPrecision](../AngularGeneralDimension/AngularGeneralDimension_AngularPrecision.md) | Gets and sets the angular precision of the dimension value. |
| [Application](../AngularGeneralDimension/AngularGeneralDimension_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadsInside](../AngularGeneralDimension/AngularGeneralDimension_ArrowheadsInside.md) | Gets and sets the ArrowheadsInside setting. |
| [Attached](../AngularGeneralDimension/AngularGeneralDimension_Attached.md) | Indicates whether this dimension is attached to anything. If not, it is considered orphaned and can be removed. |
| [AttributeSets](../AngularGeneralDimension/AngularGeneralDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionLine](../AngularGeneralDimension/AngularGeneralDimension_DimensionLine.md) | Property that returns the dimension line geometry of the dimension. |
| [DimensionType](../AngularGeneralDimension/AngularGeneralDimension_DimensionType.md) | Gets the dimension type. |
| [ExtensionLineOne](../AngularGeneralDimension/AngularGeneralDimension_ExtensionLineOne.md) | Property that returns the first extension line of the dimension. |
| [ExtensionLineOneVisible](../AngularGeneralDimension/AngularGeneralDimension_ExtensionLineOneVisible.md) | Gets and sets whether the first extension line is visible. |
| [ExtensionLineTwo](../AngularGeneralDimension/AngularGeneralDimension_ExtensionLineTwo.md) | Property that returns the second extension line of the dimension. |
| [ExtensionLineTwoVisible](../AngularGeneralDimension/AngularGeneralDimension_ExtensionLineTwoVisible.md) | Gets and sets whether the second extension line is visible. |
| [FirstArrowheadInside](../AngularGeneralDimension/AngularGeneralDimension_FirstArrowheadInside.md) | Read-write property that gets and sets whether the first arrowhead is inside or outside. |
| [FirstArrowheadType](../AngularGeneralDimension/AngularGeneralDimension_FirstArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. |
| [GeneralDimensionType](../AngularGeneralDimension/AngularGeneralDimension_GeneralDimensionType.md) | Returns an enum indicating the type of general dimension. |
| [HideSecondArrowhead](../AngularGeneralDimension/AngularGeneralDimension_HideSecondArrowhead.md) | Gets and sets whether hide the second arrowhead of the dimension. |
| [HideValue](../AngularGeneralDimension/AngularGeneralDimension_HideValue.md) | Gets and sets the HideValue setting. |
| [IntentOne](../AngularGeneralDimension/AngularGeneralDimension_IntentOne.md) | Gets and sets the first geometry associated with the dimension. |
| [IntentThree](../AngularGeneralDimension/AngularGeneralDimension_IntentThree.md) | Gets and sets the third geometry associated with the dimension. This may return Nothing in some cases where two edges or two arc end points were used for the dimension creation. |
| [IntentTwo](../AngularGeneralDimension/AngularGeneralDimension_IntentTwo.md) | Gets and sets the second geometry associated with the dimension. |
| [IsInspectionDimension](../AngularGeneralDimension/AngularGeneralDimension_IsInspectionDimension.md) | Gets and sets whether this is an inspection dimension. |
| [Layer](../AngularGeneralDimension/AngularGeneralDimension_Layer.md) | Gets and sets the layer applied to this dimension. |
| [ModelValue](../AngularGeneralDimension/AngularGeneralDimension_ModelValue.md) | Property that gets the dimension value as defined in the model or as measured in the drawing. |
| [ModelValueOverridden](../AngularGeneralDimension/AngularGeneralDimension_ModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. |
| [OppositeAngle](../AngularGeneralDimension/AngularGeneralDimension_OppositeAngle.md) | Gets and sets whether to dimension the opposite angle. |
| [OverrideModelValue](../AngularGeneralDimension/AngularGeneralDimension_OverrideModelValue.md) | Gets and sets the NominalValue setting. |
| [Parent](../AngularGeneralDimension/AngularGeneralDimension_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../AngularGeneralDimension/AngularGeneralDimension_Precision.md) | Gets and sets the Precision setting. |
| [Retrieved](../AngularGeneralDimension/AngularGeneralDimension_Retrieved.md) | Property that indicates whether the dimension was created as a result of retrieving it either from the model or a drawing view sketch. If True, the RetrievedFrom property returns the object that the dimension was retrieved from. |
| [RetrievedFrom](../AngularGeneralDimension/AngularGeneralDimension_RetrievedFrom.md) | Property that returns the object that this dimension was retrieved from. Possible return objects include all sketch constraint objects that derive from DimensionConstraint and their proxies, FeatureDimension and FeatureDimensionProxy. The property returns Nothing if the Retrieved property returns False. |
| [SecondArrowheadInside](../AngularGeneralDimension/AngularGeneralDimension_SecondArrowheadInside.md) | Read-write property that gets and sets whether the second arrowhead is inside or outside. |
| [SecondArrowheadPosition](../AngularGeneralDimension/AngularGeneralDimension_SecondArrowheadPosition.md) | Gets and sets the position of the second arrowhead. |
| [SecondArrowheadType](../AngularGeneralDimension/AngularGeneralDimension_SecondArrowheadType.md) | Read-write property that gets and sets the type of the second arrowhead. |
| [ShowLeader](../AngularGeneralDimension/AngularGeneralDimension_ShowLeader.md) | Gets and sets whether to display a leader line for the dimension text. |
| [Style](../AngularGeneralDimension/AngularGeneralDimension_Style.md) | Gets and sets the DimensionStyle associated with the dimension. |
| [Text](../AngularGeneralDimension/AngularGeneralDimension_Text.md) | Gets and sets the DimensionText setting. |
| [Tolerance](../AngularGeneralDimension/AngularGeneralDimension_Tolerance.md) | Property that returns the Tolerance object associated with this dimension. |
| [ToleranceAngularPrecision](../AngularGeneralDimension/AngularGeneralDimension_ToleranceAngularPrecision.md) | Gets and sets the angular precision of the tolerance text for the dimension. |
| [TolerancePrecision](../AngularGeneralDimension/AngularGeneralDimension_TolerancePrecision.md) | Gets and sets the precision of the tolerance text for the dimension. |
| [Type](../AngularGeneralDimension/AngularGeneralDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [UseQuadrant](../AngularGeneralDimension/AngularGeneralDimension_UseQuadrant.md) | Gets and sets whether to use the quadrant in which the input text point lies to decide which angle to dimension. |

## Accessed From

[GeneralDimensions.AddAngular](../GeneralDimensions/GeneralDimensions_AddAngular.md), [GeneralDimensions.AddAngularForeshortened](../GeneralDimensions/GeneralDimensions_AddAngularForeshortened.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Center Dimension Text](../../sample-programs/AngularGeneralDimension_CenterText_Sample.md) | This sample demonstrates how to center the text of all dimensions on the active sheet in a drawing. |

## Version

Introduced in version 11
