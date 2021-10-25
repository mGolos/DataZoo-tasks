#!/usr/bin/env python3
import streamlit as st


class Chessboard():
    '''Creates a chess board, using table ans cell widths.
    Produces an HTML local file.
    '''
    
    def __init__(self, table_width=250, cell_width=30, img_address='files/chessboard.png'):
        '''
        Keyword arguments:
        table_width -- the width of all the table in pixel (default 250)
        cell_width -- the width of all independant cells in pixel (default 30)
        img_address -- address for the resulting image (default './chessboard.png')
        '''
        import os.path
        self.table_width = table_width
        self.cell_width = cell_width
        self.img_address = img_address
        self.html_address = os.path.splitext(img_address)[0] + '.html'
        self.create_table()
        self.create_figure()
        
        
    def create_table(self):
        '''Creates a squared chessboard.
        N -- number of rows/columns depending on the ratio table_width / cell_width.
        table -- a produced 2D binary numpy.ndarray of integers type.
        '''
        from numpy import add
        
        self.N = self.table_width // self.cell_width
        self.table = add.outer(range(self.N), range(self.N)) % 2


    def create_figure(self):
        '''Creates an image file of a table using its width parameter.
        '''
        from matplotlib.pyplot import rcParams, subplots
        
        px = 1 / rcParams['figure.dpi']
        S = self.table_width * px
        
        self.fig, ax = subplots(figsize=(S,S))
        self.fig.subplots_adjust(left=0, bottom=0, right=1, top=1)
        ax.imshow(self.table, cmap="binary")
        ax.axis("off")
        
        
    def save_files(self):
        '''Saves the image and creates a simple html file displaying the produced image file.
        '''
        # image file
        self.fig.savefig(self.img_address, bbox_inches='tight', pad_inches=0)
        # html file
        with open(self.html_address, 'w') as file:
            file.write(f"<img src='{self.img_address.split('/')[-1]}'/>")
            
    
    def open_html(self):
        '''Opens the produced html file using the system.'''
        import os
        os.startfile(self.html_address, 'open')


def main():
    st.title('Task 1: Chess board')
    col1, col2 = st.columns(2)
    table_width = col1.slider('Table width:', 8, 1080, 270)
    cell_width = col2.slider('Cell width:', 1, table_width //2 , max(table_width // 9, 1))
    
    board = Chessboard(table_width=table_width, cell_width=cell_width)
    board.save_files()
    st.pyplot(board.fig)
    
    col1, col2 = st.columns(2)
    with open(board.img_address, "rb") as file:
        col1.download_button(label="Download the image file", data=file, file_name=board.img_address.split('/')[-1])
    with open(board.html_address, "rb") as file:
        col2.download_button(label="Download the html file", data=file, file_name=board.html_address.split('/')[-1])


if __name__ == '__main__':
    main()