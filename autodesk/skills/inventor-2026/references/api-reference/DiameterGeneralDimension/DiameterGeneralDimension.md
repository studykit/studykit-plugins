# DiameterGeneralDimension Object

Derived from: [GeneralDimension](../GeneralDimension/GeneralDimension.md) Object

## Description

The DiameterGeneralDimension object represents a diameter dimension placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../DiameterGeneralDimension/DiameterGeneralDimension_Delete.md) | Method that deletes the DrawingDimension. |
| [GetInspectionDimensionData](../DiameterGeneralDimension/DiameterGeneralDimension_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [GetReferenceKey](../DiameterGeneralDimension/DiameterGeneralDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [PromoteToSketch](../DiameterGeneralDimension/DiameterGeneralDimension_PromoteToSketch.md) | Method that copies the dimension to the underlying sketch. This method only works for dimensions associated with a draft view. |
| [SetInspectionDimensionData](../DiameterGeneralDimension/DiameterGeneralDimension_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn't already. |
| [ShowAllExtensionLines](../DiameterGeneralDimension/DiameterGeneralDimension_ShowAllExtensionLines.md) | Method that un-hides all the extension lines associated with this dimension. If there are no hidden extension lines associated with this dimension, this method does nothing and returns a success. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DiameterGeneralDimension/DiameterGeneralDimension_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadsInside](../DiameterGeneralDimension/DiameterGeneralDimension_ArrowheadsInside.md) | Gets and sets the ArrowheadsInside setting. |
| [Attached](../DiameterGeneralDimension/DiameterGeneralDimension_Attached.md) | Indicates whether this dimension is attached to anything. If not, it is considered orphaned and can be removed. |
| [AttributeSets](../DiameterGeneralDimension/DiameterGeneralDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionLine](../DiameterGeneralDimension/DiameterGeneralDimension_DimensionLine.md) | Property that returns the dimension line geometry of the dimension. |
| [ExtensionLineOne](../DiameterGeneralDimension/DiameterGeneralDimension_ExtensionLineOne.md) | Property that returns the first extension line of the dimension. |
| [ExtensionLineTwo](../DiameterGeneralDimension/DiameterGeneralDimension_ExtensionLineTwo.md) | Property that returns the second extension line of the dimension. |
| [FirstArrowheadInside](../DiameterGeneralDimension/DiameterGeneralDimension_FirstArrowheadInside.md) | Read-write property that gets and sets whether the first arrowhead is inside or outside. |
| [FirstArrowheadType](../DiameterGeneralDimension/DiameterGeneralDimension_FirstArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. |
| [GeneralDimensionType](../DiameterGeneralDimension/DiameterGeneralDimension_GeneralDimensionType.md) | Returns an enum indicating the type of general dimension. |
| [HideValue](../DiameterGeneralDimension/DiameterGeneralDimension_HideValue.md) | Gets and sets the HideValue setting. |
| [Intent](../DiameterGeneralDimension/DiameterGeneralDimension_Intent.md) | Gets and sets the geometry associated with the dimension. |
| [IsInspectionDimension](../DiameterGeneralDimension/DiameterGeneralDimension_IsInspectionDimension.md) | Gets and sets whether this is an inspection dimension. |
| [Layer](../DiameterGeneralDimension/DiameterGeneralDimension_Layer.md) | Gets and sets the layer applied to this dimension. |
| [LeaderFromCenter](../DiameterGeneralDimension/DiameterGeneralDimension_LeaderFromCenter.md) | Gets and sets whether the leader starts from the center of the arc or the circle. |
| [ModelValue](../DiameterGeneralDimension/DiameterGeneralDimension_ModelValue.md) | Property that gets the dimension value as defined in the model or as measured in the drawing. |
| [ModelValueOverridden](../DiameterGeneralDimension/DiameterGeneralDimension_ModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. |
| [OverrideModelValue](../DiameterGeneralDimension/DiameterGeneralDimension_OverrideModelValue.md) | Gets and sets the NominalValue setting. |
| [Parent](../DiameterGeneralDimension/DiameterGeneralDimension_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../DiameterGeneralDimension/DiameterGeneralDimension_Precision.md) | Gets and sets the Precision setting. |
| [Retrieved](../DiameterGeneralDimension/DiameterGeneralDimension_Retrieved.md) | Property that indicates whether the dimension was created as a result of retrieving it either from the model or a drawing view sketch. If True, the RetrievedFrom property returns the object that the dimension was retrieved from. |
| [RetrievedFrom](../DiameterGeneralDimension/DiameterGeneralDimension_RetrievedFrom.md) | Property that returns the object that this dimension was retrieved from. Possible return objects include all sketch constraint objects that derive from DimensionConstraint and their proxies, FeatureDimension and FeatureDimensionProxy. The property returns Nothing if the Retrieved property returns False. |
| [SecondArrowheadInside](../DiameterGeneralDimension/DiameterGeneralDimension_SecondArrowheadInside.md) | Read-write property that gets and sets whether the second arrowhead is inside or outside. |
| [SecondArrowheadType](../DiameterGeneralDimension/DiameterGeneralDimension_SecondArrowheadType.md) | Read-write property that gets and sets the type of the second arrowhead. |
| [SingleDimensionLine](../DiameterGeneralDimension/DiameterGeneralDimension_SingleDimensionLine.md) | Gets and sets whether to use a single dimension line. |
| [Style](../DiameterGeneralDimension/DiameterGeneralDimension_Style.md) | Gets and sets the DimensionStyle associated with the dimension. |
| [Text](../DiameterGeneralDimension/DiameterGeneralDimension_Text.md) | Gets and sets the DimensionText setting. |
| [Tolerance](../DiameterGeneralDimension/DiameterGeneralDimension_Tolerance.md) | Property that returns the Tolerance object associated with this dimension. |
| [TolerancePrecision](../DiameterGeneralDimension/DiameterGeneralDimension_TolerancePrecision.md) | Gets and sets the precision of the tolerance text for the dimension. |
| [Type](../DiameterGeneralDimension/DiameterGeneralDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeneralDimensions.AddDiameter](../GeneralDimensions/GeneralDimensions_AddDiameter.md)

## Derived Classes

[HoleThreadNote](../HoleThreadNote/HoleThreadNote.md)

## Version

Introduced in version 11
