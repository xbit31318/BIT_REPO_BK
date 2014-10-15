""" downloaded from http://xbmc-addons.googlecode.com/svn/addons/ """
""" addons.xml generator """

import os
import md5
import zipfile
import xml.etree.ElementTree as ET

class Generator:
    """
        Generates a new addons.xml file from each addons addon.xml file
        and a new addons.xml.md5 hash file. Must be run from the root of
        the checked-out repo. Only handles single depth folder structure.
    """
    def __init__( self ):
        # generate files
        self._generate_addons_file()
        self._generate_md5_file()
        # notify user
        print "Finished updating addons xml and md5 files"

    def _generate_addons_file( self ):
        # addon list
        dirs = os.listdir(os.getcwd())
        addons_xml = u"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<addons>\n"

        for dir in dirs:
            print dir
            if os.path.isdir(dir) == False:
                continue
            
            #addons = os.listdir( "." )
            addons = os.listdir( dir )
            # final addons text
            
            # loop thru and add each addons addon.xml file
            
            for addon in addons:
                print addon + ">>>>>>>>>>>>>>>>>"
                #print addon
                try:
                    # skip any file or .git folder
                    #if ( not os.path.isdir( addon ) or addon == ".git" ): continue
                    #print "123"
                    # create path
                    #_path = os.path.join( addon, "addon.xml" )
                    print dir + os.sep + addon + "444444444444" 
                    myzip = zipfile.ZipFile(dir + os.sep + addon)
                    
                    
                    
                    infilelist = myzip.namelist()
                    content = "123"
                    for infile in infilelist:
                        if "addon.xml" in infile:
                            content = myzip.read(infile)
                            break

                    # split lines for stripping
                    #xml_lines = content.splitlines()
                    # new addon

                    root = ET.fromstring(content)
                    addon_xml = ET.tostring(root)
                    

                    # we succeeded so add to our final addons.xml text
                    addons_xml += addon_xml.rstrip() + "\n\n"
                except Exception, e:
                    # missing or poorly formatted addon.xml
                    #print "Excluding %s for %s" % ( _path, e, )
                    print e
                    break
        # clean and add closing tag
        addons_xml = addons_xml.strip() + u"\n</addons>\n"
        # save file
        self._save_file( addons_xml.encode( "utf-8" ), file="addons.xml" )

    def _generate_md5_file( self ):
        try:
            # create a new md5 hash
            m = md5.new( open( "addons.xml" ).read() ).hexdigest()
            # save file
            self._save_file( m, file="addons.xml.md5" )
        except Exception, e:
            # oops
            print "An error occurred creating addons.xml.md5 file!\n%s" % ( e, )

    def _save_file( self, data, file ):
        try:
            # write data to the file
            open( file, "w" ).write( data )
        except Exception, e:
            # oops
            print "An error occurred saving %s file!\n%s" % ( file, e, )


if ( __name__ == "__main__" ):
    # start
    Generator()
