# DrawingSketch Object

Derived from: [Sketch](../Sketch/Sketch.md) Object

## Description

The DrawingSketch object represents a sketch within a drawing.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddArcSlotByCenterPointArc](../DrawingSketch/DrawingSketch_AddArcSlotByCenterPointArc.md) | Method that creates an arc slot. The sketch entities represent the sketch slot are returned. |
| [AddArcSlotByThreePointArc](../DrawingSketch/DrawingSketch_AddArcSlotByThreePointArc.md) | Method that creates an arc slot. The sketch entities represent the sketch slot are returned. |
| [AddByProjectingEntity](../DrawingSketch/DrawingSketch_AddByProjectingEntity.md) | Method that creates a new sketch entity by projecting other entities onto the sketch plane. This method performs the same function as the Project Geometry or Project DWG Geometry command according to the Entity you specified. |
| [AddStraightSlotByCenterToCenter](../DrawingSketch/DrawingSketch_AddStraightSlotByCenterToCenter.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [AddStraightSlotByOverall](../DrawingSketch/DrawingSketch_AddStraightSlotByOverall.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [AddStraightSlotBySlotCenter](../DrawingSketch/DrawingSketch_AddStraightSlotBySlotCenter.md) | Method that creates a straight slot. The sketch entities represent the sketch slot are returned. |
| [CopyContentsTo](../DrawingSketch/DrawingSketch_CopyContentsTo.md) | Method that copies all the contents of the sketch to the \input target sketch. |
| [CopyEntitiesTo](../DrawingSketch/DrawingSketch_CopyEntitiesTo.md) | Method that copies sketch entities of the sketch to the input target sketch. |
| [Delete](../DrawingSketch/DrawingSketch_Delete.md) | Method that deletes the sketch. This method is only valid for sketches that are not used by a feature. |
| [Edit](../DrawingSketch/DrawingSketch_Edit.md) | Method that causes the Sketch environment to be invoked with this sketch available for interactive edit. |
| [ExitEdit](../DrawingSketch/DrawingSketch_ExitEdit.md) | Causes the Sketch environment to be closed and the user interface to return to the previous environment. This is equivalent to the Return command. This method is only valid in the case where this sketch is open for edit within the user interface. |
| [GetAutomatedCenterlineSettings](../DrawingSketch/DrawingSketch_GetAutomatedCenterlineSettings.md) | Method that returns the settings that define how automatic center lines and center marks are to be calculated for this sketch. |
| [GetCustomLineType](../DrawingSketch/DrawingSketch_GetCustomLineType.md) | Method that returns information regarding the custom line type in use. The method returns a failure if the return value of the LineType property is not kCustomLineType. |
| [GetReferenceKey](../DrawingSketch/DrawingSketch_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [MoveSketchObjects](../DrawingSketch/DrawingSketch_MoveSketchObjects.md) | Method that moves a collection of sketch objects by a specified vector. If the Copy argument is set to True, the newly created objects are returned. |
| [OffsetSketchEntitiesUsingDistance](../DrawingSketch/DrawingSketch_OffsetSketchEntitiesUsingDistance.md) | Method that offsets a sketch entity or a group of connected sketch entities. In both cases, the base sketch entity is first offset by the specified distance and along the specified direction. The base sketch entity is determined as follows: \* If only one sketch entity needs to be offset, it will be treated as the base sketch entity. \* If a group of end-to-end connected entities need to be offset, the first entity in the group will be treated as the base sketch entity. If this method successfully offsets the specified input sketch entities, the newly created sketch entities are returned. |
| [OffsetSketchEntitiesUsingPoint](../DrawingSketch/DrawingSketch_OffsetSketchEntitiesUsingPoint.md) | Method that offsets a sketch entity or a group of end-to-end connected sketch entities. In both cases, the offset is first applied to the base sketch entity such that the offset of the base sketch entity passes through the specified offset point on the sketch. The shortest distance of this offset point from the original base sketch entity determines the offset distance. |
| [RotateSketchObjects](../DrawingSketch/DrawingSketch_RotateSketchObjects.md) | Method that rotates a collection of sketch objects by a specified angle. If the Copy argument is set to True, the newly created objects are returned. |
| [SetAutomatedCenterlineSettings](../DrawingSketch/DrawingSketch_SetAutomatedCenterlineSettings.md) | Method that sets the automatic centerline and center mark settings for this sketch and creates the centerlines and center marks defined by the settings. The centerlines and center marks that were created are returned. |
| [SetCustomLineType](../DrawingSketch/DrawingSketch_SetCustomLineType.md) | Method that sets a custom line type to the curve from the specified .lin file. The method automatically changes the value of LineType property to kCustomLineType. |
| [SheetToSketchSpace](../DrawingSketch/DrawingSketch_SheetToSketchSpace.md) | Method that takes a coordinate in sheet space returns a Point2d object containing the resulting coordinate point in sketch space. |
| [SketchToSheetSpace](../DrawingSketch/DrawingSketch_SketchToSheetSpace.md) | Method that takes a coordinate in sketch space, and returns a Point2d object containing the coordinates of the point in sheet space. |
| [Solve](../DrawingSketch/DrawingSketch_Solve.md) | Method that causes the sketch to solve. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../DrawingSketch/DrawingSketch_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../DrawingSketch/DrawingSketch_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [CircularPatterns](../DrawingSketch/DrawingSketch_CircularPatterns.md) | Gets the SketchCircularPatterns collection object. |
| [Color](../DrawingSketch/DrawingSketch_Color.md) | Gets and Sets the color for the sketch. |
| [ConstraintStatus](../DrawingSketch/DrawingSketch_ConstraintStatus.md) | Property that returns an enum indicating the constraint status of the sketch entity, signifying whether it is fully constrained, over constrained, or under constrained. |
| [DataIO](../DrawingSketch/DrawingSketch_DataIO.md) | Gets the object through which this sketch's data content can be persisted. |
| [DeferUpdates](../DrawingSketch/DrawingSketch_DeferUpdates.md) | Gets and Sets whether to defer the solving of the sketch or not. |
| [DimensionConstraints](../DrawingSketch/DrawingSketch_DimensionConstraints.md) | Gets the collection of all dimension constraints on the sketch. |
| [DisabledActionTypes](../DrawingSketch/DrawingSketch_DisabledActionTypes.md) | Gets and sets the action types valid for this sketch. |
| [GeometricConstraints](../DrawingSketch/DrawingSketch_GeometricConstraints.md) | Property that returns the collection of all geometric constraints on the sketch. |
| [LineType](../DrawingSketch/DrawingSketch_LineType.md) | Gets and Sets the line type override for the sketch. |
| [LineWeight](../DrawingSketch/DrawingSketch_LineWeight.md) | Gets and Sets the line weight override for the sketch. |
| [Name](../DrawingSketch/DrawingSketch_Name.md) | Gets and sets name of the sketch. |
| [Parent](../DrawingSketch/DrawingSketch_Parent.md) | Property that gets the parent object from whom this object can logically be reached. |
| [Profiles](../DrawingSketch/DrawingSketch_Profiles.md) | Gets the profiles collection associated with this drawing sketch. |
| [RectangularPatterns](../DrawingSketch/DrawingSketch_RectangularPatterns.md) | Gets the SketchRectangularPatterns collection object. |
| [SketchArcs](../DrawingSketch/DrawingSketch_SketchArcs.md) | Property that returns the SketchArcs collection object. |
| [SketchCircles](../DrawingSketch/DrawingSketch_SketchCircles.md) | Property that returns the SketchArcs collection object. |
| [SketchControlPointSplines](../DrawingSketch/DrawingSketch_SketchControlPointSplines.md) | Read-only property that returns the SketchControlPointSplines collection object. This collection provides access to the existing control point splines in the sketch and provides functionality to create new control point splines. |
| [SketchEllipses](../DrawingSketch/DrawingSketch_SketchEllipses.md) | Property that returns the SketchEllipses collection object. |
| [SketchEllipticalArcs](../DrawingSketch/DrawingSketch_SketchEllipticalArcs.md) | Property that returns the SketchEllipticalArcs collection object. |
| [SketchEntities](../DrawingSketch/DrawingSketch_SketchEntities.md) | Property that returns the collection of all entities on the sketch, regardless of their type. |
| [SketchEquationCurves](../DrawingSketch/DrawingSketch_SketchEquationCurves.md) | Read-only property that returns the SketchEquationCurves collection object. This collection provides access to the existing equation curves in the sketch and provides functionality to create new equation curves. |
| [SketchFillRegions](../DrawingSketch/DrawingSketch_SketchFillRegions.md) |  |
| [SketchFixedSplines](../DrawingSketch/DrawingSketch_SketchFixedSplines.md) | Property that gets the collection object. |
| [SketchHatchRegions](../DrawingSketch/DrawingSketch_SketchHatchRegions.md) | Read-only property that returns the SketchHatchRegions collection object. |
| [SketchImages](../DrawingSketch/DrawingSketch_SketchImages.md) | Property that returns a collection of all images on the sketch. |
| [SketchLines](../DrawingSketch/DrawingSketch_SketchLines.md) | Property that returns the SketchLines collection object. This collection provides access to the existing lines in the sketch and provides functionality to create new lines. |
| [SketchOffsetSplines](../DrawingSketch/DrawingSketch_SketchOffsetSplines.md) | Property that returns the collection object. This collection provides access to the existing offset splines in the sketch. |
| [SketchPoints](../DrawingSketch/DrawingSketch_SketchPoints.md) | Property that returns the SketchPoints collection object. |
| [SketchSplines](../DrawingSketch/DrawingSketch_SketchSplines.md) | Property that returns the SketchSplines collection object. |
| [TextBoxes](../DrawingSketch/DrawingSketch_TextBoxes.md) | Gets the TextBoxes collection associated with this Sketch. |
| [Type](../DrawingSketch/DrawingSketch_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [Visible](../DrawingSketch/DrawingSketch_Visible.md) | Gets and sets the visibility of the sketch. |

## Accessed From

[BorderDefinition.Edit](../BorderDefinition/BorderDefinition_Edit.md), [BorderDefinition.Sketch](../BorderDefinition/BorderDefinition_Sketch.md), [BreakOperation.BreakLineSketch](../BreakOperation/BreakOperation_BreakLineSketch.md), [CropOperation.CropBoundarySketch](../CropOperation/CropOperation_CropBoundarySketch.md), [DrawingSketches.Add](../DrawingSketches/DrawingSketches_Add.md), [DrawingSketches.Item](../DrawingSketches/DrawingSketches_Item.md), [RevisionCloud.Sketch](../RevisionCloud/RevisionCloud_Sketch.md), [SectionDrawingView.SectionLineSketch](../SectionDrawingView/SectionDrawingView_SectionLineSketch.md), [SketchedSymbolDefinition.Edit](../SketchedSymbolDefinition/SketchedSymbolDefinition_Edit.md), [SketchedSymbolDefinition.Sketch](../SketchedSymbolDefinition/SketchedSymbolDefinition_Sketch.md), [SketchHatchRegion.Parent](../SketchHatchRegion/SketchHatchRegion_Parent.md), [TitleBlockDefinition.Edit](../TitleBlockDefinition/TitleBlockDefinition_Edit.md), [TitleBlockDefinition.Sketch](../TitleBlockDefinition/TitleBlockDefinition_Sketch.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create BreakOpertion by Sketch Sample](../../sample-programs/CreateBreakOpertionBySketchSample_Sample.md) | This sample demonstrates how to create a break operation using a sketch. |
| [Drawing Sketches - editing line type and color](../../sample-programs/DrawingSketch_Sample.md) | This sample demonstrates the modification of sketch entity line type and color in drawings. |
| [Sketch fill region](../../sample-programs/DrawingSketch_SketchFillRegions_Sample.md) | This sample demonstrates the sketch fill functionality in drawing sketches. |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |

## Version

Introduced in version 5.3
