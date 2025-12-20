# Sheet Object

## Description

The Sheet object represents a sheet in a drawing document. See here for an overview on drawing views.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Activate](../Sheet/Sheet_Activate.md) | Method that causes this sheet to become the active sheet. |
| [AddBorder](../Sheet/Sheet_AddBorder.md) | Method that adds the specified border definition to the sheet. This method will fail in the case where a border instance already exists on the sheet. In this case, use the Delete method of the Border object to remove the existing one first. |
| [AddDefaultBorder](../Sheet/Sheet_AddDefaultBorder.md) | Method that adds an instance of the default border to the sheet. This method is the equivalent of inserting the 'Default Border' border. A border created using the default border is created 'on the fly' by Autodesk Inventor using the supplied input. It is not based on an existing border definition. |
| [AddTitleBlock](../Sheet/Sheet_AddTitleBlock.md) | Method that adds the specified title block definition to the sheet. Since a sheet can only have one title block at a time, calling this method will remove the existing title block. |
| [ChangeLayer](../Sheet/Sheet_ChangeLayer.md) | Method that changes the associated layer for all the input objects. |
| [CopyTo](../Sheet/Sheet_CopyTo.md) | Method that copies this sheet into the specified drawing document. The new sheet is returned. |
| [CreateGeometryIntent](../Sheet/Sheet_CreateGeometryIntent.md) | Method that creates a GeometryIntent object for use in various annotation and view creations. |
| [Delete](../Sheet/Sheet_Delete.md) | Method that deletes this sheet. |
| [FindUsingPoint](../Sheet/Sheet_FindUsingPoint.md) | Method that finds drawing curve segments, entities on a sheet sketch, centerlines and centermarks that the given point lies on. |
| [GetAvailableDesignViewsToRetrieve3DAnnotations](../Sheet/Sheet_GetAvailableDesignViewsToRetrieve3DAnnotations.md) | Gets an array of strings containing names of the design views of model document that the 3D annotations can be retrieved from. |
| [GetReferenceKey](../Sheet/Sheet_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetRetrievableAnnotations](../Sheet/Sheet_GetRetrievableAnnotations.md) | Returns a collection of objects that represent the valid set of model dimensions that can be retrieved into the input drawing view. |
| [RetrieveAnnotations](../Sheet/Sheet_RetrieveAnnotations.md) | Retrieves sketch and/or model annotations into the drawing. |
| [Update](../Sheet/Sheet_Update.md) | Method that updates the sheet. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../Sheet/Sheet_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../Sheet/Sheet_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [AutoCADBlocks](../Sheet/Sheet_AutoCADBlocks.md) | Property that returns the AutoCADBlocks collection object. This object provides access to all instances of AutoCAD blocks on a sheet. This property returns Nothing for sheets on an Inventor IDW document. |
| [Balloons](../Sheet/Sheet_Balloons.md) | Property that returns the collection of on this sheet. |
| [Border](../Sheet/Sheet_Border.md) | Property that returns the Border or DefaultBorder object associated with the sheet. This property will return Nothing in the case where the sheet doesn't have a border. |
| [Centerlines](../Sheet/Sheet_Centerlines.md) | Property that returns the Centerlines collection object. |
| [Centermarks](../Sheet/Sheet_Centermarks.md) | Property that returns the Centermarks collection object. |
| [ClientGraphicsCollection](../Sheet/Sheet_ClientGraphicsCollection.md) | Gets the ClientGraphicsCollection object. |
| [ClientViews](../Sheet/Sheet_ClientViews.md) | Property that returns the collection for the drawing sheet. |
| [CustomTables](../Sheet/Sheet_CustomTables.md) | Property that returns the CustomTables collection object for this sheet. |
| [DataIO](../Sheet/Sheet_DataIO.md) | Property that returns a DataIO object. The DataIO object can be used to write out the sheet data in various formats. The Sheet currently only supports |
| [DrawingDimensions](../Sheet/Sheet_DrawingDimensions.md) | Property that returns the DrawingDimensions collection object. This object provides access to all of the dimensions on the sheet. |
| [DrawingNotes](../Sheet/Sheet_DrawingNotes.md) | Property that returns the DrawingNotes collection object consisting of all drawing notes. |
| [DrawingViews](../Sheet/Sheet_DrawingViews.md) | Property that returns the collection object. This provides access to the existing drawing views on the sheet. |
| [EdgeSymbols](../Sheet/Sheet_EdgeSymbols.md) | Read-only property that returns the collection of edge symbols on this sheet. |
| [ExcludeFromCount](../Sheet/Sheet_ExcludeFromCount.md) | Gets or sets whether to exclude the sheet in the count of sheets in the drawing. |
| [ExcludeFromPrinting](../Sheet/Sheet_ExcludeFromPrinting.md) | Gets or sets whether to exclude the sheet when printing the drawing. |
| [FeatureControlFrames](../Sheet/Sheet_FeatureControlFrames.md) | Property that returns the FeatureControlFrames collection object. |
| [GraphicsDataSetsCollection](../Sheet/Sheet_GraphicsDataSetsCollection.md) | Gets the GraphicsDataSetsCollection object. |
| [Height](../Sheet/Sheet_Height.md) | Gets or sets the height of the sheet. |
| [HoleTables](../Sheet/Sheet_HoleTables.md) | Property that returns the HoleTables collection object. |
| [IsModelSpaceSheet](../Sheet/Sheet_IsModelSpaceSheet.md) | Property that returns whether this is a model space sheet created automatically when opening (rather than importing) AutoCAD dwg files. |
| [Name](../Sheet/Sheet_Name.md) | Gets or sets the user-friendly name of the Sheet. |
| [Orientation](../Sheet/Sheet_Orientation.md) | Gets or sets the orientation of the sheet as it is viewed or printed. |
| [Parent](../Sheet/Sheet_Parent.md) | Property returning the parent document. When used within Autodesk Inventor the DrawingDocument object will be returned. When used within Apprentice the ApprenticeServerDrawingDocument object will be returned. |
| [PartsLists](../Sheet/Sheet_PartsLists.md) | Property that returns the PartsLists collection object associated with this sheet. This provides access to the existing parts lists on the sheet. |
| [Revision](../Sheet/Sheet_Revision.md) | Gets or sets the revision number of the sheet. |
| [RevisionClouds](../Sheet/Sheet_RevisionClouds.md) | Get the RevisionClouds collection object. |
| [RevisionTables](../Sheet/Sheet_RevisionTables.md) | Property that returns the RevisionTables collection object. |
| [Size](../Sheet/Sheet_Size.md) | Gets or sets the size of the Sheet as value in an enumeration of standard sheet sizes. |
| [SketchedSymbols](../Sheet/Sheet_SketchedSymbols.md) | Property that returns the SketchedSymbols collection object. This object provides access to all sketched symbols on a sheet. |
| [Sketches](../Sheet/Sheet_Sketches.md) | Property that returns the DrawingSketches collection object for the sheet. This object provides access to all of the sketches that have been created on the sheet and provides functionality to create new sketches. |
| [Status](../Sheet/Sheet_Status.md) | Property that returns the current status of the sheet and its contents. If the value is equal to kUpToDateDrawingSheet then the drawing sheet is up to date. Any other value means some portion of the sheet is out of date. The returned value can contain status information about several things about the sheet. You can use bitwise operators to determine the status for a particular item. For example the following can be used to see if the precise display for views on sheet are up to date. If (oSheet.Status And kProcessingPreciseDisplayDrawingSheet) = kProcessingPreciseDisplayDrawingSheet Then MsgBox "Processing precise display." End If This is useful when an operation requires the sheet to be up to date. For example, when plotting the sheet. |
| [SurfaceTextureSymbols](../Sheet/Sheet_SurfaceTextureSymbols.md) | Property that returns the SurfaceTextureSymbols collection object. |
| [TextPropertySource](../Sheet/Sheet_TextPropertySource.md) | Read-write property that gets and sets the text property source model. This is the name of a drawing view. |
| [TitleBlock](../Sheet/Sheet_TitleBlock.md) | Property that returns the TitleBlock object associated with the sheet. This property will return Nothing in the case where the sheet doesn't have a title block. |
| [TransitionSymbols](../Sheet/Sheet_TransitionSymbols.md) | Returns the collection of edge symbols on this sheet. |
| [Type](../Sheet/Sheet_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |
| [WeldingSymbols](../Sheet/Sheet_WeldingSymbols.md) | Get the DrawingWeldingSymbols collection object. |
| [Width](../Sheet/Sheet_Width.md) | Gets or sets the width of the sheet. |

## Accessed From

[AngularGeneralDimension.Parent](../AngularGeneralDimension/AngularGeneralDimension_Parent.md), [AutoCADBlock.Parent](../AutoCADBlock/AutoCADBlock_Parent.md), [Balloon.Parent](../Balloon/Balloon_Parent.md), [BaselineDimensionSet.Parent](../BaselineDimensionSet/BaselineDimensionSet_Parent.md), [BendNote.Parent](../BendNote/BendNote_Parent.md), [Border.Parent](../Border/Border_Parent.md), [Centerline.Parent](../Centerline/Centerline_Parent.md), [Centermark.Parent](../Centermark/Centermark_Parent.md), [ChainDimensionSet.Parent](../ChainDimensionSet/ChainDimensionSet_Parent.md), [ChamferNote.Parent](../ChamferNote/ChamferNote_Parent.md), [DefaultBorder.Parent](../DefaultBorder/DefaultBorder_Parent.md), [DetailDrawingView.Parent](../DetailDrawingView/DetailDrawingView_Parent.md), [DiameterGeneralDimension.Parent](../DiameterGeneralDimension/DiameterGeneralDimension_Parent.md), [DrawingDimension.Parent](../DrawingDimension/DrawingDimension_Parent.md), [DrawingDocument.ActiveSheet](../DrawingDocument/DrawingDocument_ActiveSheet.md), [DrawingNote.Parent](../DrawingNote/DrawingNote_Parent.md), [DrawingView.Parent](../DrawingView/DrawingView_Parent.md), [DrawingWeldingSymbol.Parent](../DrawingWeldingSymbol/DrawingWeldingSymbol_Parent.md), [EdgeSymbol.Parent](../EdgeSymbol/EdgeSymbol_Parent.md), [FeatureControlFrame.Parent](../FeatureControlFrame/FeatureControlFrame_Parent.md), [GeneralDimension.Parent](../GeneralDimension/GeneralDimension_Parent.md), [GeneralNote.Parent](../GeneralNote/GeneralNote_Parent.md), [HoleTable.Parent](../HoleTable/HoleTable_Parent.md), [HoleThreadNote.Parent](../HoleThreadNote/HoleThreadNote_Parent.md), [LeaderNote.Parent](../LeaderNote/LeaderNote_Parent.md), [LinearGeneralDimension.Parent](../LinearGeneralDimension/LinearGeneralDimension_Parent.md), [OrdinateDimension.Parent](../OrdinateDimension/OrdinateDimension_Parent.md), [OrdinateDimensionSet.Parent](../OrdinateDimensionSet/OrdinateDimensionSet_Parent.md), [PartsList.Parent](../PartsList/PartsList_Parent.md), [PunchNote.Parent](../PunchNote/PunchNote_Parent.md), [RadiusGeneralDimension.Parent](../RadiusGeneralDimension/RadiusGeneralDimension_Parent.md), [RevisionTable.Parent](../RevisionTable/RevisionTable_Parent.md), [SectionDrawingView.Parent](../SectionDrawingView/SectionDrawingView_Parent.md), [Sheet.CopyTo](../Sheet/Sheet_CopyTo.md), [Sheets.Add](../Sheets/Sheets_Add.md), [Sheets.AddUsingSheetFormat](../Sheets/Sheets_AddUsingSheetFormat.md), [Sheets.Item](../Sheets/Sheets_Item.md), [SketchedSymbol.Parent](../SketchedSymbol/SketchedSymbol_Parent.md), [SurfaceTextureANSIDefinition.Parent](../SurfaceTextureANSIDefinition/SurfaceTextureANSIDefinition_Parent.md), [SurfaceTextureBSIDefinition.Parent](../SurfaceTextureBSIDefinition/SurfaceTextureBSIDefinition_Parent.md), [SurfaceTextureDINDefinition.Parent](../SurfaceTextureDINDefinition/SurfaceTextureDINDefinition_Parent.md), [SurfaceTextureGBDefinition.Parent](../SurfaceTextureGBDefinition/SurfaceTextureGBDefinition_Parent.md), [SurfaceTextureGOSTDefinition.Parent](../SurfaceTextureGOSTDefinition/SurfaceTextureGOSTDefinition_Parent.md), [SurfaceTextureISODefinition.Parent](../SurfaceTextureISODefinition/SurfaceTextureISODefinition_Parent.md), [SurfaceTextureJISDefinition.Parent](../SurfaceTextureJISDefinition/SurfaceTextureJISDefinition_Parent.md), [SurfaceTextureSymbol.Parent](../SurfaceTextureSymbol/SurfaceTextureSymbol_Parent.md), [SurfaceTextureSymbolDefinition.Parent](../SurfaceTextureSymbolDefinition/SurfaceTextureSymbolDefinition_Parent.md), [TitleBlock.Parent](../TitleBlock/TitleBlock_Parent.md), [TransitionSymbol.Parent](../TransitionSymbol/TransitionSymbol_Parent.md)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [AutoCAD block insertion](../../sample-programs/AutoCADBlocks_Add_Sample.md) | Demonstrates inserting an AutoCAD block. |
| [Balloons - edit](../../sample-programs/Balloons_Sample.md) | This sample demonstrates the editing of balloons in a drawing. |
| [Creation a balloon](../../sample-programs/Balloons_Add_Sample.md) | This sample demonstrates the creation of a balloon. |
| [Baseline dimension sets](../../sample-programs/BaselineDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a baseline set dimension in a drawing. |
| [Create bend note](../../sample-programs/BendNotes_Add_Sample.md) | This sample demonstrates the creation of a bend note on the drawing view of a flat pattern. |
| [Creation of a break operation in a drawing view](../../sample-programs/BreakOperations_Add_Sample.md) | Demonstrates the creation of a break operation. |
| [Chain dimensions sets](../../sample-programs/ChainDimensionSets_Add_Sample.md) | This sample demonstrates the creation of a chain dimension set in a drawing. |
| [Custom Table - create](../../sample-programs/CustomTables_Sample.md) | This sample demonstrates how to create a custom table. |
| [Create a Bend Table](../../sample-programs/CustomTables_AddBendTable_Sample.md) | This sample demonstrates the creation of a bend table in a drawing from a sheet metal part. |
| [Create a Configuration Table](../../sample-programs/CustomTables_AddConfigurationTable_Sample.md) | This sample demonstrates the creation of a configuration (iPart/iAssembly) table in a drawing from a factory document. |
| [Create a drawing Excel Table](../../sample-programs/CustomTables_AddExcelTable_Sample.md) | This sample demonstrates the creation of a table based on an Excel file in a drawing. |
| [Adding and editing a feature control frame](../../sample-programs/FeatureControlFrame_FeatureControlFrameRows_Sample.md) | These samples demonstrate editing an existing feature control frame symbol. The first sample adds a row to an existing symbol. The second sample replaces all rows of an existing symbol. |
| [Create thread note](../../sample-programs/HoleThreadNotes_Add_Sample.md) | This sample demonstrates the creation of a thread note on a drawing view. |
| [Creating a parts list](../../sample-programs/PartsLists_Add_Sample.md) | This sample demonstrates the creation of a parts list. The parts list is placed at the top right corner of the border if one exists, else it is placed at the top right corner of the sheet. |
| [create punch note](../../sample-programs/PunchNotes_Add_Sample.md) | This sample demonstrates the creation of a punch note on the drawing view of a flat pattern. |
| [Border Insert](../../sample-programs/Sheet_AddDefaultBorder_Sample.md) | This sample illustrates inserting a default border. |
| [Border Insert Default](../../sample-programs/Sheet_AddDefaultBorder2_Sample.md) | This sample illustrates inserting a default border using the default values. |
| [Create sheet with multiple views](../../sample-programs/SheetFormat_Sample.md) | This sample demonstrates the creation of a drawing sheet based on a particular sheet format containing the definition for multiple views. |
| [Create SketchedSymbol Definition](../../sample-programs/SketchedSymbolDefinition_Sample.md) | This sample illustrates creating a new sketched symbol definition object and inserting it into the active sheet. |
| [Create sketched symbol and leader](../../sample-programs/SketchedSymbols_AddWithLeader_Sample.md) | This sample illustrates creating sketched symbol with a leader. |
| [Add surface texture symbol to dimension](../../sample-programs/SurfaceTextureSymbols_Add_Sample.md) | This sample demonstrates the creation of a surface texture symbol attached to the extension line of a drawing dimension. |
| [Sketch Text Add](../../sample-programs/TextBoxes_Sample.md) | This sample illustrates creating text in a sketch. |
| [Title Block Definition Create and Insert](../../sample-programs/TitleBlockDefinition_Sample.md) | This sample illustrates creating a new title block definition object and inserting it into the active sheet. This sample consists of two subs. The first demonstrates the creation of a title block definition and the second inserts it into the active sheet. |
| [Copying a title block definition](../../sample-programs/TitleBlockDefinition_CopyTo_Sample.md) | This sample demonstrates copying a title block definition from one drawing to another and replacing the existing title blocks in the drawing with the new title block. |

## Version

Introduced in version 4

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |