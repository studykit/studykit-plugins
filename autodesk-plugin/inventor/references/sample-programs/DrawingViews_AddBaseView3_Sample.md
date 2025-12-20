# Create base view with representations

## Description

This sample demonstrates how to create a base view by specifying various representations.

## Code Samples

* [C#](#C#)

Before running this sample, make sure that the file C:\temp\Reps.iam exists (or change the path in the sample). The file must contain a level of detail representation named MyLODRep, a positional representation named MyPositionalRep and a design view representation named MyDesignViewRep. The first line of the C# sample sets the oApp variable to ThisApplication - this should be appropriately changed.

|  |
| --- |
| Copy Code |

```
public void AddBaseViewWithRepresentations()
{
    Application oApp = ThisApplication;

    // Set a reference to the drawing document.
    // This assumes a drawing document is active.
    DrawingDocument oDrawDoc = (DrawingDocument)oApp.ActiveDocument;

    //Set a reference to the active sheet.
    Sheet oSheet = oDrawDoc.ActiveSheet;

    // Create a new NameValueMap object
    NameValueMap oBaseViewOptions = oApp.TransientObjects.CreateNameValueMap();

    // Set the representations to use when creating the base view.
    oBaseViewOptions.Add("PositionalRepresentation", "MyPositionalRep");
    oBaseViewOptions.Add("DesignViewRepresentation", "MyDesignViewRep");
    oBaseViewOptions.Add("DesignViewAssociative", true);

    // Open the model document (corresponding to the "MyLODRep" representation).
    String strFullDocumentName = oApp.FileManager.GetFullDocumentName("C:\temp\Reps.iam", "MyLODRep");
    Document oModel = oApp.Documents.Open(strFullDocumentName, false);

    // Create the placement point object.
    Point2d oPoint = oApp.TransientGeometry.CreatePoint2d(25, 25);

    // Create a base view.
    DrawingView oBaseView = oSheet.DrawingViews.AddBaseView((_Document)oModel, oPoint, 2,
                                        ViewOrientationTypeEnum.kIsoTopLeftViewOrientation,
                                        DrawingViewStyleEnum.kHiddenLineRemovedDrawingViewStyle,
                                        "", null, oBaseViewOptions);

    // Release reference of the invisibly open model
    oModel.ReleaseReference();

}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |