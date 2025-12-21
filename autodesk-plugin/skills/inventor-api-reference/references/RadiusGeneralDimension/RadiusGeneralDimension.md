# RadiusGeneralDimension Object

Derived from: [GeneralDimension](../GeneralDimension/GeneralDimension.md) Object

## Description

The RadiusGeneralDimension object represents a radial general dimension placed on a sheet.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RadiusGeneralDimension/RadiusGeneralDimension_Delete.md) | Method that deletes the DrawingDimension. |
| [GetInspectionDimensionData](../RadiusGeneralDimension/RadiusGeneralDimension_GetInspectionDimensionData.md) | Method that returns the data associated with an inspection dimension. This method returns an error if the IsInspectionDimension property returns False. |
| [GetReferenceKey](../RadiusGeneralDimension/RadiusGeneralDimension_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [PromoteToSketch](../RadiusGeneralDimension/RadiusGeneralDimension_PromoteToSketch.md) | Method that copies the dimension to the underlying sketch. This method only works for dimensions associated with a draft view. |
| [SetInspectionDimensionData](../RadiusGeneralDimension/RadiusGeneralDimension_SetInspectionDimensionData.md) | Method that sets the data associated with an inspection dimension. This method automatically sets the IsInspectionDimension property to True, if it isn't already. |
| [ShowAllExtensionLines](../RadiusGeneralDimension/RadiusGeneralDimension_ShowAllExtensionLines.md) | Method that un-hides all the extension lines associated with this dimension. If there are no hidden extension lines associated with this dimension, this method does nothing and returns a success. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../RadiusGeneralDimension/RadiusGeneralDimension_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ArrowheadsInside](../RadiusGeneralDimension/RadiusGeneralDimension_ArrowheadsInside.md) | Gets and sets the ArrowheadsInside setting. |
| [Attached](../RadiusGeneralDimension/RadiusGeneralDimension_Attached.md) | Indicates whether this dimension is attached to anything. If not, it is considered orphaned and can be removed. |
| [AttributeSets](../RadiusGeneralDimension/RadiusGeneralDimension_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [DimensionLine](../RadiusGeneralDimension/RadiusGeneralDimension_DimensionLine.md) | Property that returns the dimension line geometry of the dimension. |
| [FirstArrowheadInside](../RadiusGeneralDimension/RadiusGeneralDimension_FirstArrowheadInside.md) | Read-write property that gets and sets whether the first arrowhead is inside or outside. |
| [FirstArrowheadType](../RadiusGeneralDimension/RadiusGeneralDimension_FirstArrowheadType.md) | Read-write property that gets and sets the type of the first arrowhead. |
| [GeneralDimensionType](../RadiusGeneralDimension/RadiusGeneralDimension_GeneralDimensionType.md) | Returns an enum indicating the type of general dimension. |
| [HideValue](../RadiusGeneralDimension/RadiusGeneralDimension_HideValue.md) | Gets and sets the HideValue setting. |
| [Intent](../RadiusGeneralDimension/RadiusGeneralDimension_Intent.md) | Gets and sets the geometry associated with the dimension. |
| [IsInspectionDimension](../RadiusGeneralDimension/RadiusGeneralDimension_IsInspectionDimension.md) | Gets and sets whether this is an inspection dimension. |
| [Jogged](../RadiusGeneralDimension/RadiusGeneralDimension_Jogged.md) | Gets and sets whether the dimension is jogged. |
| [Layer](../RadiusGeneralDimension/RadiusGeneralDimension_Layer.md) | Gets and sets the layer applied to this dimension. |
| [LeaderFromCenter](../RadiusGeneralDimension/RadiusGeneralDimension_LeaderFromCenter.md) | Gets and sets whether the leader starts from the center of the arc or the circle. |
| [ModelValue](../RadiusGeneralDimension/RadiusGeneralDimension_ModelValue.md) | Property that gets the dimension value as defined in the model or as measured in the drawing. |
| [ModelValueOverridden](../RadiusGeneralDimension/RadiusGeneralDimension_ModelValueOverridden.md) | Read-write property that gets and sets whether the model value is overridden for the dimension. |
| [OverrideModelValue](../RadiusGeneralDimension/RadiusGeneralDimension_OverrideModelValue.md) | Gets and sets the NominalValue setting. |
| [Parent](../RadiusGeneralDimension/RadiusGeneralDimension_Parent.md) | Property that returns the parent sheet of the object. |
| [Precision](../RadiusGeneralDimension/RadiusGeneralDimension_Precision.md) | Gets and sets the Precision setting. |
| [Retrieved](../RadiusGeneralDimension/RadiusGeneralDimension_Retrieved.md) | Property that indicates whether the dimension was created as a result of retrieving it either from the model or a drawing view sketch. If True, the RetrievedFrom property returns the object that the dimension was retrieved from. |
| [RetrievedFrom](../RadiusGeneralDimension/RadiusGeneralDimension_RetrievedFrom.md) | Property that returns the object that this dimension was retrieved from. Possible return objects include all sketch constraint objects that derive from DimensionConstraint and their proxies, FeatureDimension and FeatureDimensionProxy. The property returns Nothing if the Retrieved property returns False. |
| [SecondArrowheadInside](../RadiusGeneralDimension/RadiusGeneralDimension_SecondArrowheadInside.md) | Read-write property that gets and sets whether the second arrowhead is inside or outside. |
| [SecondArrowheadType](../RadiusGeneralDimension/RadiusGeneralDimension_SecondArrowheadType.md) | Read-write property that gets and sets the type of the second arrowhead. |
| [Style](../RadiusGeneralDimension/RadiusGeneralDimension_Style.md) | Gets and sets the DimensionStyle associated with the dimension. |
| [Text](../RadiusGeneralDimension/RadiusGeneralDimension_Text.md) | Gets and sets the DimensionText setting. |
| [Tolerance](../RadiusGeneralDimension/RadiusGeneralDimension_Tolerance.md) | Property that returns the Tolerance object associated with this dimension. |
| [TolerancePrecision](../RadiusGeneralDimension/RadiusGeneralDimension_TolerancePrecision.md) | Gets and sets the precision of the tolerance text for the dimension. |
| [Type](../RadiusGeneralDimension/RadiusGeneralDimension_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[GeneralDimensions.AddRadius](../GeneralDimensions/GeneralDimensions_AddRadius.md)

## Version

Introduced in version 11

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |